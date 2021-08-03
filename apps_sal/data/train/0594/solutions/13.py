# cook your dish here
n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
total = sum(a)
current_max = a[0]
total_max = a[0]
for i in range(1, len(a)):
    current_max = max(a[i], current_max + a[i])
    total_max = max(total_max, current_max)
print(total - total_max + (total_max / x))
