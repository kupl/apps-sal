def one_down(txt):

    if type(txt) is not str:
        return "Input is not a string"

    new_string = ""
    for char in txt:
        if char == " ":
            new_string = new_string + " "
        elif char == "A":
            new_string = new_string + "Z"
        elif char == "a":
            new_string = new_string + "z"
        elif char in "-+,.;:":
            new_string = new_string + char
        else:
            new_string = new_string + chr(ord(char) - 1)
    return new_string
