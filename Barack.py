from os import listdir, system
from PIL import Image as im, ImageDraw as imdrw
from random import randint, choice



def diffTuples(t1, i, j)->tuple:
	c = [t1[0], t1[0], t1[0]]
	c[j] = t1[j] - i

	return (c[0], c[1], c[2])

def dist(t1, t2):
	c = []

	c.append(abs(t1[0] - t2[0]))
	c.append(abs(t1[1] - t2[1]))
	c.append(abs(t1[2] - t2[2]))
	
	return (c[0], c[1], c[2])

system("cls")

PATH = "D:/Drive/test"
SCALE = 50 # Taille des carrés
DIVS = 150 # Nombre d'images en hauteurs

if __name__ == "__main__":
	files = listdir(f"{PATH}")
	print(f"{len(files)} images loaded from {PATH}/...")
	# files2 = [files[n] for n in range(len(files)//2)]
	images = {}
	c = 0
	for file in files:
		print(f"{int(c/len(files)*100)}% of the image(s) processed", end="\r")
		c+=1
		imgb = im.open(f"{PATH}/{file}")
		imgr =  im.new("RGB", (SCALE, SCALE))
		cW, cH = imgb.size
		R, G, B = 0, 0, 0

		for x in range(SCALE):
			for y in range(SCALE):
				size = min(cH, cW)
				coords = int(x/SCALE * size), int(y/SCALE*size)
				color = imgb.getpixel(coords)
				imgr.putpixel((x, y), color)
				R += color[0]
				G += color[1]
				B += color[2]

		R//=SCALE**2
		G//=SCALE**2
		B//=SCALE**2

		if (R, G, B) not in images:
			images[(R, G, B)] = []
		images[(R, G, B)].append(imgr)
		

	ref = im.open(f"{PATH}/IMG_20201002_181635_480.jpg")
	print(f"{PATH}/IMG_20201002_181635_480.jpg loaded")
	refW, refH = ref.size
	W, H = DIVS * refW // refH, DIVS
	res = im.new("RGB", (W * SCALE, H * SCALE))

	ctx = imdrw.Draw(res)
	for x in range(W):
		for y in range(H):
			coords = int(x/W*refW), int(y/H*refH)
			c = ref.getpixel(coords)
			x1 = x * SCALE 
			y1 = y * SCALE 
			x2 = (x+1) * SCALE 
			y2 = (y+1) * SCALE
			for j in range(3):
				for i in range(-120, 120):
					if dist(c, diffTuples(c, i, j)) <= (1, 1, 1):
						if diffTuples(c, i, j) in images:
							res.paste(choice((images[diffTuples(c, i, j)])), (x1, y1))

print(f"Creating {PATH}.png...")
res.save(PATH + ".png")
print(f"Opening {PATH}.png...")
system(PATH + ".png")