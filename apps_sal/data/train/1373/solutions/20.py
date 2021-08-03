import sys
from collections import defaultdict
def fin(): return sys.stdin.readline().strip()
def fout(s, end="\n"): sys.stdout.write(str(s) + end)


t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, fin().split()))
    a = [int(x) for x in fin().split()]
    freq = defaultdict(int)
    freq[a[0]] += 1
    temp = set([a[0]])
    ans = 1
    prev = 0
    for i in range(1, n):

        freq[a[i]] += 1
        temp.add(a[i])

        if len(temp) < k:
            ans = max(ans, i - prev + 1)
        else:
            while len(temp) >= k:
                freq[a[prev]] -= 1
                if freq[a[prev]] == 0:
                    temp.remove(a[prev])
                prev += 1

    print(ans)
