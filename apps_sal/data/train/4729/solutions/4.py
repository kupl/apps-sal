NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def numbers_of_letters(n):
    s = ''.join(NUM[i] for i in map(int, str(n)))
    return [s] + (numbers_of_letters(len(s)) if len(s) != n else [])
