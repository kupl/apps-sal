def check(a, b, i, n):
    for j in range(i + 1, n):
        if a[j] == '0' and b[j] == '1':
            return j
    return -1


for _ in range(int(input())):
    n = int(input())
    (a, b) = (input(), input())
    for i in range(n):
        if a[i] != b[i]:
            if a[i] == 0:
                print('No')
                break
            else:
                x = check(a, b, i, n)
                if x == -1:
                    print('No')
                    break
                else:
                    a = a[:i] + a[x] + a[i + 1:x] + a[i] + a[x + 1:]
    else:
        print('Yes')
