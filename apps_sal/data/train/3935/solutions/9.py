def vowel_recognition(input):
    vl = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    n = len(input)
    count = 0
    for (num, letter) in enumerate(input):
        for vowel in vl:
            if letter == vowel:
                x = num + 1
                count += x * (n - x + 1)
    return count
