import re


def is_audio(filename):
    return bool(re.match(r"[a-zA-Z]+\.(mp3|([fa]l|a)ac)$", filename))


def is_img(filename):
    return bool(re.match(r"[a-zA-Z]+\.(jpe?g|png|bmp|gif)$", filename))
