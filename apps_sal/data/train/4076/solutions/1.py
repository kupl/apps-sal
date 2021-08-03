def get_count(words=''):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    v, c = 0, 0
    try:
        for l in words.lower():
            if l in vowels:
                v += 1
            elif l in consonants:
                c += 1
        return {"vowels": v, "consonants": c}
    except:
        return {"vowels": 0, "consonants": 0}
