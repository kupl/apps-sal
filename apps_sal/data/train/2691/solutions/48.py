def solve(s):
    for letter in s:
        if letter.isdigit():
            pass
        else:
            s = s.replace(letter, ' ')
    numberList = map(int, s.split())
    return max(numberList)
