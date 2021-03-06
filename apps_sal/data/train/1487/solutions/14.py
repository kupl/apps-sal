for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    (left, right) = (0, n - 1)
    (c1, c2) = (0, 0)
    (b1, b2) = (0, 0)
    while left <= right:
        if c1 < x * c2:
            c1 += arr[left]
            left += 1
            b1 += 1
        elif c1 > x * c2:
            c2 += arr[right]
            right -= 1
            b2 += 1
        elif left != right:
            c1 += arr[left]
            left += 1
            b1 += 1
        elif b1 < b2:
            c2 += arr[right]
            right -= 1
            b2 += 1
        else:
            c1 += arr[left]
            left += 1
            b1 += 1
    print(b1, b2)
