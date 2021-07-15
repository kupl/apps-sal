from collections import Counter
n=int(input())
arr1=list(map(int,input().split()))[:n]
arr2=list(map(int,input().split()))[:n+1]
c1 = Counter(arr1)
# print(c1)
c2 = Counter(arr2)
# print(c2)
diff = list((c2 - c1).elements())
print(*diff)
