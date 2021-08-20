def string_counter(string, char):
    return sum((1 for i in string if char == i))
