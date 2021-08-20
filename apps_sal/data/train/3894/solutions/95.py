def solve(s):
    up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_up = 0
    letter_low = 0
    for letter in s:
        if letter in up:
            letter_up += 1
        elif letter in low:
            letter_low += 1
    if letter_up > letter_low:
        return s.upper()
    else:
        return s.lower()
