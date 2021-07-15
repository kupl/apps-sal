def to_freud(sentence):
  words = sentence.split(" ")
  return " ".join(["sex" for i in range(len(words))]) 
