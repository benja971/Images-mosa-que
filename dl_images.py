from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyCtzVaBxxBR6JFphMOuAm3P2HvWtr9Pe0E', '1414e3890e57991f2')

# define search params:
# _search_params = {
#     'q': 'horse',
#     'num': 10,
#     'safe': 'high|medium|off',
#     'fileType': 'jpg|png',
#     'imgType': 'clipart|face|lineart|news|photo',
#     'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
#     'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow',
#     'imgColorType': 'color',
#     'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
# }
_search_params = {
    'q': 'cat',
    'num': 15,
    'safe': 'off',
    'fileType': 'jpg',
    'imgType': 'photo',
    'imgSize': 'MEDIUM',
    'imgDominantColor': 'green',
    'imgColorType': 'color',
    'rights': 'cc_publicdomain'
}

# this will only search for images:
# gis.search(search_params=_search_params)

# this will search and download:
# gis.search(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
# gis.search(search_params=_search_params, path_to_dir='/images/', width=500, height=500)

# search first, then download and resize afterwards:
gis.search(search_params=_search_params)
for image in gis.results():
    image.download('./images/')
    # image.resize(500, 500)