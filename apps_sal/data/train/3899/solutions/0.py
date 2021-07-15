def guess_my_number(guess, number = '123-451-2345'):
    return "".join(c if c in guess+"-" else "#" for c in number)

