for _i in range(int(input())):
 x,k = list(map(int,input().split()))
 a = list(map(int,input().split()))
 b = list(map(int,input().split()))
 l = []
 l.append(x)
 for i in range(k):
  x = x+(x*(float(a[i])/b[i]))
 w = l[0]
 perc = 100*(float(w)/x)
 ans = 100-perc
 print(int(ans))




