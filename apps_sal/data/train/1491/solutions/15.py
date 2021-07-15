a,b,c,d = list(map(float, input().strip().split()))
if a/b == c/d or a/b == d/c:
 print('Possible')
elif a/c == b/d or a/c == d/b:
 print('Possible')
elif a/d == c/b or a/d == b/c:
 print('Possible')
else:
 print('Impossible')

