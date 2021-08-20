def solve(arr):

    def cou(arg):
        al = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        num = 0
        arg = ''.join(arg).lower()
        for x in range(len(arg)):
            if x + 1 == al[arg[x]]:
                num += 1
        return num
    res = []
    for x in range(len(arr)):
        res.append(cou(arr[x]))
    return res
