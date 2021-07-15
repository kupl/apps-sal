from datetime import date
li = ['','january', 'february', 'march', 'april', 'may',
 'june', 'july', 'august', 'september', 'october', 'november', 'december']
t = int(input())
for j in range(t):
 a=list(input().split())
 d=int(a[0])
 m=li.index(a[1])
 if m==2 and d==29:
  print('30 august')
 elif m<=2:
  td = date(2020,m,d)
  td1 = date(2021,m,d)
  diff = (td1-td)/2
  ans = td+diff
  ad,am = ans.day,ans.month
  print(ad,li[am])
 else:
  td = date(2019,m,d)
  td1 = date(2020,m,d)
  diff = (td1-td)/2
  ans = td+diff
  ad,am = ans.day,ans.month
  print(ad,li[am])

