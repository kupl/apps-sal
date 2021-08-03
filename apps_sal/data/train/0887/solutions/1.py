# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a[0] != 0 or b[-1] != 0 or a[-1] != b[0]:
        print('No')

    else:
        ab = b[0]
        flag = 0
        for i in range(1, n - 1):
            if a[i] == 0 or b[i] == 0:
                print('No')
                flag = 1
                break

            elif a[i] + b[i] < ab:
                print('No')
                flag = 1
                break

            elif a[i] > ab + b[i] or b[i] > ab + a[i]:
                print('No')
                flag = 1
                break

        if flag == 0:
            print('Yes')
