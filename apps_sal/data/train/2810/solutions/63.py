from string import ascii_lowercase


def solve(arr):
    alphabet = list(ascii_lowercase)
    return_arr = []
    for i in arr:
        count = 0
        for j in range(0, len(i)):
            if j == alphabet.index(i[j].lower()):
                count += 1
        return_arr.append(count)
    return return_arr
