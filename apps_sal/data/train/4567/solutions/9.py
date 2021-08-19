def pillow(s):
    return bool([1 for (fridge, pillow) in zip(s[0], s[1]) if fridge == 'n' and pillow == 'B'])
