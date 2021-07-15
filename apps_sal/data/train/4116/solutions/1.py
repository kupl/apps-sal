import re
def is_audio(file_name):
    return bool(re.match(r'^[A-Za-z]+\.(mp3|flac|alac|aac)$', file_name))

def is_img(file_name):
    return bool(re.search(r'^[A-Za-z]+\.(jpg|jpeg|png|bmp|gif)$', file_name))
