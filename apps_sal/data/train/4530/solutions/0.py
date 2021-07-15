def consonant_count(str):
    return sum(1 for c in str if c.isalpha() and c.lower() not in "aeiou")

