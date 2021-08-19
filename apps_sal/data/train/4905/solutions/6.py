def answer(puzzlebox):
    print(dir(puzzlebox))
    print(puzzlebox.hint)
    print(puzzlebox.hint_two)
    print(puzzlebox.key)
    print(puzzlebox.lock(puzzlebox.key))
    return 42
