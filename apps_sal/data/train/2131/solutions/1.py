m = 1000000007
n = int(input())
a = input().split()
print(pow(2, n - 1, m) - 1 - sum((pow(2, a.count(x), m) - 1 for x in set(a) if x != '-1')) % m)
