import sys
for _ in range(int(sys.stdin.readline())):
    (n, k) = [int(i) for i in sys.stdin.readline().split()]
    word = sys.stdin.readline().strip()
    ans = 0
    for col in ['RGB', 'GBR', 'BRG']:
        cnt = 0
        for i in range(k):
            if word[i] == col[i % 3]:
                cnt += 1
        mx = cnt
        for i in range(n - k):
            if word[i + k] == col[(i + k) % 3]:
                cnt += 1
            if word[i] == col[i % 3]:
                cnt -= 1
            if cnt > mx:
                mx = cnt
        ans = max(ans, mx)
    sys.stdout.write(str(k - ans) + '\n')
