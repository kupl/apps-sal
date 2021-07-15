# cook your dish here
for _ in range(int(input())):
 f, b, l, r, t, d = input().split()
 ans = False
 #front
 if (f == l or f == r) and (f == t or f == d): ans = True
 #back
 if (b == l or b == r) and (b == t or b == d): ans = True
 #top
 if (t == l or t == r) and (t == f or t == b): ans = True
 #down
 if (d == l or d == r) and (d == f or d == b): ans = True
 #left
 if (l == f or l == b) and (l == t or l == d): ans = True
 #right
 if (r == f or r == b) and (r == t or r == d): ans = True
 print("YES" if ans else "NO")
 

