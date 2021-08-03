def match(file_name, exts): return [name.isalpha() and ext in exts for name, ext in [file_name.rsplit('.', 1)]][0]
def is_audio(file_name): return match(file_name, ['mp3', 'flac', 'alac', 'aac'])
def is_img(file_name): return match(file_name, ['jpg', 'jpeg', 'png', 'bmp', 'gif'])
