t = int(input())

for i in range(t):
    l = int(input())
    nums = list(map(int, input().split()))

    if l == 1:
        print(0)
        continue

    even, odd = 0, 0

    for n in nums:
        if n % 2 == 0:
            even += 1

        else:
            odd += 1

    less, more = 0, 0

    if even >= odd:
        less = odd
        more = even

    else:
        less = even
        more = odd

    if less > 0:
        print((less - 1) * 2 + more)

    else:
        print(more)
