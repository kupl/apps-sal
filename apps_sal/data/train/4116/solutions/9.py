import re


def make_matcher(exts):
    def match(s):
        name, ext = s.split('.')
        return name.isalpha() and ext in exts
    return match


is_audio = make_matcher('mp3 flac alac aac'.split())

is_img = make_matcher('jpg jpeg gif png bmp'.split())
