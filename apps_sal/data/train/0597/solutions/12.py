# cook your dish here
for _ in range(int(input())):
 n = int(input())
 x1, h1 = map(int, input().split())
 x2, h2 = map(int, input().split())
 l1 = [x2-x1]
 l2 = [h1, h2]
 for i in range(2, n):
  x, h = map(int, input().split())
  l1.append(x-x1)
  l2.append(h)
  x1 = x2
  x2 = x
 l1.append(x2-x1)
 l1.sort()
 l2.sort()
 a = 0
 for i in range(n):
  a += l1[i]*l2[i]
 print(a)
