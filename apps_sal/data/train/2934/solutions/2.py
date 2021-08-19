def solve(s):
    count = 0
    max = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in s:
        if letter in vowels:
            if count > max:
                max = count
            count = 0
        else:
            count += int(ord(letter)) - 96
    return max
