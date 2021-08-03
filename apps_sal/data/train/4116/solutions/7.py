def c(x, f): return bool(__import__('re').match(r'([a-zA-Z]+\.({}))'.format("|".join(x)), f))


def is_audio(f): return c(['mp3', 'flac', 'alac', 'aac'], f)
def is_img(f): return c(['jpg', 'jpeg', 'png', 'bmp', 'gif'], f)
