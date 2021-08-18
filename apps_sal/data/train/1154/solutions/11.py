from collections import Counter
n = int(input())

arr = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

print(sum(arr2) - sum(arr))
