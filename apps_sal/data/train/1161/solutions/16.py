for _ in range(int(input())):
    string = list(input())
    s = string.count('s')
    m = string.count('m')
    for i in range(len(string) - 1):
        if (string[i], string[i + 1]) in (('m', 's'), ('s', 'm')):
            string[i] = 'd'
            string[i + 1] = 'd'
            s -= 1
    print('mongooses') if m > s else print('snakes') if s > m else print('tie')
