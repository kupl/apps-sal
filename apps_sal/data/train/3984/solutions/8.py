ing = {"t": "tomato", "l": "lettuce", "c": "cheese", "g": "guacamole", "s": "salsa", "a": "beef", "|": "shell"}

def tacofy(word):
    return [ing[c] for c in "|{}|".format("".join(c if c in "tlcgs" else "a" if c in "aeiou" else "" for c in word.lower()))]
