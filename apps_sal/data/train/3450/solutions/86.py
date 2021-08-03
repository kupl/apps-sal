def array(string):
    print(string)
    if string.count(",") < 2:
        return None
    string = string.replace(",", " ")

    front = 0
    for letter in string:
        front += 1
        if letter == " ":
            break
    back = 0
    for letter in reversed(string):
        back += 1
        if letter == " ":
            break

    return string[front:-back]
