def vowel_indices(word):
    word = word.lower()
    vowels = ['a','e','i','o','u','y']
    vowel_indicies = []
    for i in range (len(word)):
      if word[i] in vowels:
        vowel_indicies.append(i + 1)
      else:
        pass
    return vowel_indicies
      

