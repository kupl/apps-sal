m = 10**9+7;a = [0]*(10**5+10);a[0] = 1
for i in range(1,10**5+5):a[i] = (a[i-1]*(i*(2*i-1)%m)%m)
for _ in range(int(input())):print(a[int(input())])
