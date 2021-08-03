from collections import Counter
n = int(input())
array = list(map(int, input().split()))
print(n - Counter(array).most_common(1)[0][1])
