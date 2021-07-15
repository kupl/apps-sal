# cook your dish here
total, diff = list(map(int, input().split()))
l1 = [int(input()) for m in range(total)]
count = 0
l1.sort()
i = 0
while (i<total-1):
 if l1[i+1] - l1[i] <= diff:
  count += 1
  i += 2
 else:
  i += 1

print(count)

