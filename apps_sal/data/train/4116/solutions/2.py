import re


def has_ext(p): return (lambda f: bool(re.match(fr"[a-zA-Z]+\.({p})$", f)))


is_audio = has_ext("mp3|([fa]l|a)ac")
is_img = has_ext("jpe?g|png|bmp|gif")
