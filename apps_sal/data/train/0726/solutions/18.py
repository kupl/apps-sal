# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 list1 = []
 l = []
 for i in range(n):
  x = input()
  list1.extend(list(x))
 for i in ('codehf'):
  l.append(list1.count(i))
 l[0] = l[0]/2
 l[3] = l[3]/2
 print(int(min(l)))

