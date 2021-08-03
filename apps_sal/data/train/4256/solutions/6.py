def insert_missing_letters(s):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    memo = {}
    for char in s:
        if char not in memo:
            memo[char] = 1
        else:
            memo[char] += 1
        if memo[char] == 1:
            res += char + "".join(sorted(list(set(alph[alph.index(char.upper()) + 1:]) - set(s.upper()))))
        else:
            res += char
    return res
