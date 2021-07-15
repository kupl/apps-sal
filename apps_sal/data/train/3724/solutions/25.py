def hero(bullets, dragons):
    if dragons==0: return False
    if bullets/dragons>2 or bullets/dragons==2 or dragons==0 : return True
    else: return False
