def solve(arr):
    from string import ascii_lowercase as alphabet
    (count, total) = (0, [])
    for word in arr:
        for (c, letter) in enumerate(word[0:26].lower()):
            if letter == alphabet[c]:
                count += 1
        total.append(count)
        count = 0
    return total
