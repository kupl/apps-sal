def solve(arr):
    alphabet = {chr(i + 96): i for i in range(1, 27)}
    arr_list = []
    for word in arr:
        ct = 0
        for (pos, letter) in enumerate(word.lower(), 1):
            if alphabet[letter] == pos:
                ct += 1
        arr_list.append(ct)
    return arr_list
