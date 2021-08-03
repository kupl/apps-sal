from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(str, input().split())))
    count = Counter(arr).most_common(1)
    print(max(count)[0])
