reverse=lambda s:__import__('re').sub(r'(.)\1+',lambda x:x.group(0).swapcase(),s)
