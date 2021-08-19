for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    left, right = 0, n - 1
    c1, c2 = 0, 0
    b1, b2 = 0, 0
    while left <= right:
        if c1 < x * c2:
            # print('h1')
            c1 += arr[left]
            left += 1
            b1 += 1
        elif c1 > x * c2:
            # print('h2')
            c2 += arr[right]
            right -= 1
            b2 += 1
        else:
            if left != right:
                # print('h3')
                c1 += arr[left]
                left += 1
                b1 += 1
            else:
                if b1 < b2:
                    # print('h4')
                    c2 += arr[right]
                    right -= 1
                    b2 += 1
                else:
                    # print('h5')
                    c1 += arr[left]
                    left += 1
                    b1 += 1
    print(b1, b2)
