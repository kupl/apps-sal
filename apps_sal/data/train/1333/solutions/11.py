t = int(input());
for i in range(t):
 n = int(input());
 a = list([int(j) for j in input().split()]);
 count = 1;
 res = 1;
 if n > 1:
  for j in range(n-1):
   if a[j+1]|a[j] > a[j+1]:
    res = 0;
    break;
   x = str(bin(a[j+1])[2:]).count('1');
   y = str(bin(a[j+1]-a[j])[2:]).count('1');
   count *= pow(2,x-y,1000000007);
   count %= 1000000007;
 if res == 0:
  print(0%1000000007);
 else:
  print(count%1000000007);
