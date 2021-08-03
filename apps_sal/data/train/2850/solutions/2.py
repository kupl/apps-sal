def gordon(a):
    return " ".join(word.upper().translate(str.maketrans("AEIOU", "@****"))
                    + "!!! !"  for word in a.split())
