t = int(input())
for _ in range(t):
    k = int(input())
    count = 1
    for i in range(k):
        for j in range(i + 1):
            if i < k - 1:
                if i == j or j == 0:
                    print(count, end='')
                    count += 1
                else:
                    print(' ', end='')
            else:
                print(count, end='')
                count += 1
        print()
