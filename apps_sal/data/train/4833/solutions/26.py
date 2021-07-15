def replace_exclamation(s):
  vowels = "aeiouAEIOU"
  output = ""
  for c in s:
    if c in vowels:
      output += "!"
    else:
      output += c
  return output
