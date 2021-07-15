def count_vowels(s = '',count=0,vowels='aeiou'):
    if type(s) is str:
        for i in s.lower():
            if i in vowels:
                count+=1
        return count
    else:
        return None
