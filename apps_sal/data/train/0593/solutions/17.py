import string
s = string.ascii_lowercase
for _ in range(int(input())):
 arr = list(map(int, input().split()))
 s1 = input()
 total = 0
 for i in s:
  if i not in s1:
   total += arr[s.index(i)]
   s1 += i
 print(total)

