def tacofy(word):
    tacos = {"a": "beef", "e": "beef", "i": "beef", "o": "beef", "u": "beef", "t": "tomato", "l": "lettuce", "c": "cheese", "g": "guacamole", "s": "salsa"}
    return ["shell"] + [tacos[c.lower()] for c in word if c.lower() in tacos] + ["shell"]
