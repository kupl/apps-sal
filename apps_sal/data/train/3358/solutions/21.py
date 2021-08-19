def correct(string):
    corrected = {'0': 'O', '1': 'I', '3': 'E', '5': 'S', '7': 'T'}
    for char in string:
        for (num, alpha) in corrected.items():
            if char == num:
                string = string.replace(char, alpha)
    return string
