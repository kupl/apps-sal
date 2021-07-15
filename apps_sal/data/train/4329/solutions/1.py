def pig_latin(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = s.lower()
    if not word.isalpha():    # Check for non alpha character
        return None
    if word[0] in vowels:     # Check if word starts with a vowel
        return word + 'way'
    for i, letter in enumerate(word):    # Find the first vowel and add the beginning to the end 
        if letter in vowels:
            return word[i:]+word[:i]+'ay'
    return word + 'ay'    # No vowels
