def binary_search(b, item, n):
    lb = 0
    a = b[:]
    ub = n - 1
    cnt = 1
    f = 0
    while lb <= ub:
        mid = (lb + ub) // 2
        if a[mid] == item:
            f = 1
            a.pop(mid)
            ub = ub - 1
            cnt = cnt + 1
        elif a[mid] > item:
            ub = mid - 1
        else:
            lb = mid + 1

    if f == 1:
        return cnt
    else:
        return False


cases = int(input())
for v in range(cases):
    a = list(map(int, input().strip().split()))
    n = a[0]
    x = a[1]
    a = list(map(int, input().strip().split()))

    cnt = 0

    for i in range(1, n + 1):
        if x % i == 0:
            side = i
            freq = 0
            subsetsum = []
            left = 0
            right = i - 1
            s = sum(a[:right + 1])
            if s > x:
                freq = freq + 1
            else:
                subsetsum.append(s)
            while right < n - 1:
                right += 1
                s = s + a[right] - a[left]
                left += 1

                if s > x:
                    freq = freq + 1
                else:
                    subsetsum.append(s)

            y = x // side
            subsetsum.sort()

            for r in range(n - side + 1 - freq):
                h = binary_search(subsetsum, y - subsetsum[r], n - side + 1 - freq)
                if h:
                    cnt = cnt + h - 1

    print(cnt)


# a = [1,2,3,4,5]
# n = 5
# for i in range(1,6):
#     print(i)
#     left = 0
#     right = i-1
#     subset = []
#     s = sum(a[:right+1])
#     subset.append(s)
#     while right < n-1:
#         right += 1
#         s = s + a[right] - a[left]
#         left += 1
#         subset.append(s)

#     print(subset)
