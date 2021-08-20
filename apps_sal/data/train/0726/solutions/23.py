for _ in range(int(input())):
    s = ''
    for i in range(int(input())):
        s += input()
    counts = []
    counts.append(s.count('c') // 2)
    counts.append(s.count('e') // 2)
    counts.append(s.count('o'))
    counts.append(s.count('d'))
    counts.append(s.count('h'))
    counts.append(s.count('f'))
    print(min(counts))
