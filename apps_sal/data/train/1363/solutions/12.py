MOD = 10**9+7
tcase = eval(input())
for times in range(tcase):
 rep, digit = list(map(int,input().split()))
 number = str(int(str(digit)*rep)**2)
 mult = 1
 ans = 0
 for dig in number:
  ans += ((int(dig)%MOD)*mult)%MOD
  mult = ((mult%MOD)*23)%MOD
 print(ans%MOD)
