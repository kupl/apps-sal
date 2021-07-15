import re
remove_chars = lambda s: re.sub('[^a-zA-Z\ ]', '', s)

