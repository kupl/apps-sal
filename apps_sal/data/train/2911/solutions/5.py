def count_vowels(s = ''):
    vowels = ["a","e","o","u","i"]
    counter = 0
    try:
        s = s.lower() 
        for char in s:
            if char in vowels:
                counter +=1
        return counter
    except AttributeError:
        return None
