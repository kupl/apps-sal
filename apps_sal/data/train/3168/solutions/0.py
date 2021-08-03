def grabscrab(said, possible_words):
    return [word for word in possible_words if sorted(word) == sorted(said)]
