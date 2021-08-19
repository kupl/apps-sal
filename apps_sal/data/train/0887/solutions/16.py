try:
    t = int(input())
    for case in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        yes = True
        if a[0] != 0 or b[n - 1] != 0:
            print('No')
            yes = False
        elif a[n - 1] != b[0]:
            print('No')
            yes = False
        else:
            for edge in range(1, n - 1):
                if a[edge] == 0 or b[edge] == 0:
                    print('No')
                    yes = False
                    break
                elif a[edge] + b[edge] < b[0]:
                    print('No')
                    yes = False
                    break
                elif a[edge] + b[0] < b[edge]:
                    print('No')
                    yes = False
                    break
                elif a[n - 1] + b[edge] < a[edge]:
                    print('No')
                    yes = False
                    break
        if yes:
            print('Yes')
except EOFError:
    pass
