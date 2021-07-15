def luck_check(string):
    e0, b1 = len(string) // 2, (len(string) + 1) // 2
    return sum(map(int, string[:e0])) == sum(map(int, string[b1:]))
