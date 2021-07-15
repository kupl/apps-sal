def bucket_of(said):
    said = said.lower()
    forgiven_words = lambda *words: any(w in said for w in words)
    water = forgiven_words("water", "wet", "wash")
    slime = forgiven_words("i don't know", "slime")
    return ["air", "water", "slime", "sludge"][2*slime + water]
