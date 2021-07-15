arithmetic=lambda a,b,o:__import__("operator").__dict__[o[:3].replace('div','truediv')](a,b)
