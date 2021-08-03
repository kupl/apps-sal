def stringy(size):
    string = "1"
    for number, index in enumerate(range(0, size - 1)):
        print(string)
        if index % 2 == 0:
            string = string + "0"
        else:
            string = string + "1"
    return string
