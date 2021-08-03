import re


def is_audio(file_name):
    return bool(re.match(r'[a-zA-Z]+(\.(mp3|flac|alac|aac))', file_name))


def is_img(file_name):
    return bool(re.match(r'[a-zA-Z]+(\.(jpg|jpeg|png|bmp|gif))', file_name))
