from collections import Counter
#inputlist = list(input().split())
n = int(input())
list1 = list(map(int, input().split()))[:n]
list1 = sorted(list1)
list2 = list(map(int, input().split()))[:n + 1]
list2 = sorted(list2)
cnt1 = Counter(list1)
cnt2 = Counter(list2)
print(*list((cnt2 - cnt1).elements()))
