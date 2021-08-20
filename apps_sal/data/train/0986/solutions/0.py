t = int(input())
while t > 0:
    t = t - 1
    (n, k) = list(map(int, input().split()))
    a = [0] * n
    done = True

    def swap(z):
        for j in range(0, n):
            if a[j] == 0:
                a[j] = z
                done = True
                break
            elif a[j] > z:
                swap(j)
                a[j] = z
            else:
                done = False
                break
    for i in range(0, n):
        for j in range(0, n):
            if abs(i - j) == k:
                if a[j] == 0:
                    a[j] = i + 1
                    done = True
                    break
                elif a[j] > i + 1:
                    swap(a[j])
                    a[j] = i + 1
                else:
                    done = False
    if 0 in a:
        print('CAPTAIN AMERICA EVADES')
    elif done:
        for c in a:
            print(c, end=' ')
        print()
    else:
        print('CAPTAIN AMERICA EVADES')
