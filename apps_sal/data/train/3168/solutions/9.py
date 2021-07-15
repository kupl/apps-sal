def grabscrab(word, possible_words):
    return [wd for wd in possible_words if sorted(word) == sorted(wd)]
        

