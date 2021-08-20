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
            for r in range(n - side + 1 - freq):
                for c in range(n - side + 1 - freq):
                    if subsetsum[r] + subsetsum[c] == x // side:
                        cnt += 1
    print(cnt)
