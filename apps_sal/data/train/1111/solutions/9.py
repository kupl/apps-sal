for _ in range(int(input())):
    N = int(input())
    count = 0
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        print('0')
    else:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] + arr[j]) % 2 != 0:
                    count += 1
        print(count)
