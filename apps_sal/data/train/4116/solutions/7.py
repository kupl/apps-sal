c = lambda x,f: bool(__import__('re').match(r'([a-zA-Z]+\.({}))'.format("|".join(x)),f))
is_audio=lambda f:c(['mp3','flac','alac','aac'],f)
is_img=lambda f:c(['jpg','jpeg','png','bmp','gif'],f)
