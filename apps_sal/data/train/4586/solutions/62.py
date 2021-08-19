def tv_remote(word):
    print(word)
    remote = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    second = find(remote, word[0])
    clicks = second[0] + second[1] + 1
    for i in range(len(word) - 1):
        first = find(remote, word[i])
        second = find(remote, word[i + 1])
        clicks += abs(second[0] - first[0])
        clicks += abs(second[1] - first[1]) + 1
    return clicks


def find(list, v):
    for (i, x) in enumerate(list):
        if v in x:
            return (i, x.index(v))
