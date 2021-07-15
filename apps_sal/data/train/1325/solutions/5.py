t = int(input())
while t:
 a,b,c,d = list(map(int , input().split()))
 app = ((a-b) + c) // 2
 mng = a - app
 org = d - (app + mng)
 print(app,mng,org)
 t = t - 1
