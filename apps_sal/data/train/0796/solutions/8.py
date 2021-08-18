
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    prev = 0
    end = 0
    arr.append(0)
    for i in range(n):
        if i >= end:
            prev = 1
        else:
            prev -= 1
            print(prev, end=' ')
            continue
        for j in range(i, n):
            if arr[j] * arr[j + 1] < 0:
                prev += 1
            else:
                break
        end = j
        print(prev, end=' ')
    print()
