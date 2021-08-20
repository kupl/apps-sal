def ind(w):
    a = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == w:
                return (i, j)


def tv_remote(word):
    press = sum(ind(word[0])) + len(word)
    for i in range(len(word) - 1):
        (f_i, f_j) = ind(word[i])
        (s_i, s_j) = ind(word[i + 1])
        press += abs(f_i - s_i) + abs(f_j - s_j)
    return press
