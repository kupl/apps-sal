A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for _ in range(int(input())):
    s = input()
    l = []
    count = 0
    if len(s) == 0:
        print(0)
    else:
        for i in s:
            if (i in A) and (i not in l):
                l.append(i)
                count += 1
        print(count)
