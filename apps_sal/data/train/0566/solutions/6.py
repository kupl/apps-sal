for _ in range(int(input())):
    (s1, s2) = (input(), input())
    for i in s1:
        if i in s2:
            print('Yes')
            break
    else:
        print('No')
