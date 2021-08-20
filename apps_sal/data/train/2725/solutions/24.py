def gimme(input_array):
    (a, b, c) = input_array
    return 2 if a < c < b or a > c > b else a < b < c or a > b > c
