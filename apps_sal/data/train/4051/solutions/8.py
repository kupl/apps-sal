def toUnderScore(name):

    list_of_chars = []
    previous_char = None

    for char in name:

        if previous_char is not None and char != "_" and previous_char != "_":

            if char.isupper() or char.isdigit() and not previous_char.isdigit():
                list_of_chars.append("_")

        list_of_chars.append(char)
        previous_char = char

    return "".join(list_of_chars)
