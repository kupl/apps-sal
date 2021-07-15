def reverse(st: str) -> str:
    """ Reverse the words in a given string. """
    return " ".join(list(filter(lambda it: it, st.split(" ")))[::-1])
