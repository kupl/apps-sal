def answer(puzzlebox):
    # Print statements are your friend.
    print(dir(puzzlebox))
    # print(puzzlebox.answer)
    print(puzzlebox.hint)
    print(puzzlebox.hint_two)
    print(puzzlebox.key)
    print(puzzlebox.lock(puzzlebox.key))
    return 42
