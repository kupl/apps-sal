t = int(input())
for tc in range(t):
    n = int(input())
    stem = ''
    arr = input().split()
    size = len(arr[0])
    max_length = 0
    for i in range(size):
        for j in range(i, size + 1):
            temp = arr[0][i:j]
            check = True
            for x in range(1, n):
                if temp in arr[x]:
                    pass
                else:
                    check = False
            if check:
                if max_length < j - i + 1:
                    stem = temp
                    max_length = j - i + 1
                elif max_length == j - i + 1 and stem > temp:
                    stem = temp
    print(stem)
