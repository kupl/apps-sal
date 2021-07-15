for _ in range(int(input())):
 a = input().split()
 n = int(a[0])
 k = int(a[1])
 s = sorted(map(int, input().split()), reverse = True)
 i = k
 while i<n and s[i]==s[k-1]:
  i+=1
 print(i)
