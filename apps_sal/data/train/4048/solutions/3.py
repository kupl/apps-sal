def pig_latin(word):
    if len(word) > 3:
      ay = word[0] + "ay"
      ans = word[1:]+ay
      return ans
    else:
      return word
