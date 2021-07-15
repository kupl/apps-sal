match = lambda file_name, exts: [name.isalpha() and ext in exts for name, ext in [file_name.rsplit('.', 1)]][0]
is_audio = lambda file_name: match(file_name, ['mp3', 'flac', 'alac', 'aac'])
is_img = lambda file_name: match(file_name, ['jpg', 'jpeg', 'png', 'bmp', 'gif'])
