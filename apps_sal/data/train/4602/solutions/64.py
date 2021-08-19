# write the function is_anagram
def is_anagram(test, original):
    for i in test:
        if i.lower() in original.lower() and len(test) == len(original):
            continue
        return False
    return True
