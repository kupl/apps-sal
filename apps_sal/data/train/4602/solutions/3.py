# In one line then
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())  # Compare, returns either true or false
