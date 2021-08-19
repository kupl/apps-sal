try:
    for t in range(int(input())):
        k = int(input().strip(' '))
        kc = input().split(' ')
        for q in range(int(input())):
            (q1, q2) = input().split(' ')
            q1 = int(q1)
            q2 = int(q2)
            sum = 0
            for i in range(q1 - 1, q2):
                sum = sum + int(kc[i].strip())
            print(sum)
except EOFError as e:
    pass
