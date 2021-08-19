q = int(input())
for test_case in range(q):
    n = int(input())
    t = input().split()
    if n == 1:
        print(1)
        print(1)
        continue
    t_0 = t[0]
    all_same = True
    any_adj_same = False
    adj_same_index = -1
    for i in range(0, len(t)):
        animal = t[i]
        if animal != t_0:
            all_same = False
        if animal == t[(i + 1) % n]:
            any_adj_same = True
            adj_same_index = i
    if all_same:
        print(1)
        output = ''
        for i in range(n):
            output += ' 1'
        output = output[1:]
        print(output)
        continue
    if n % 2 == 0:
        print(2)
        output = ''
        for i in range(n):
            output += ' 1' if i % 2 == 0 else ' 2'
        output = output[1:]
        print(output)
        continue
    if any_adj_same:
        print(2)
        output = ''
        for i in range(n):
            if i > adj_same_index:
                output += ' 2' if i % 2 == 0 else ' 1'
            else:
                output += ' 1' if i % 2 == 0 else ' 2'
        output = output[1:]
        print(output)
        continue
    else:
        print(3)
        output = ''
        for i in range(n - 1):
            output += '1 ' if i % 2 == 0 else '2 '
        output += '3'
        print(output)
        continue
