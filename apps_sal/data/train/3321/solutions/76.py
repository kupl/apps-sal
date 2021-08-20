def evil(n):
    s = []
    length = (n + 2) // 2
    for i in range(length):
        r = n % 2
        s.append(r)
        if n // 2 == 0:
            break
        n = n // 2
    s_reverse = s[::-1]
    binary = ''
    for n in s_reverse:
        binary += str(n)
    count = 0
    for s in binary:
        if s == '1':
            count += 1
    if count % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
