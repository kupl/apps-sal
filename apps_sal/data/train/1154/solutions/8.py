# cook your dish here
n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
print(sum(brr) - sum(arr))
