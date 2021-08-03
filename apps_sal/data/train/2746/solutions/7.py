def check_vowel(string, position):
    string = string + '             '
    vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if string[position] in vowles:
        return True
    else:
        return False
