a, b , c, d = list(map(int , input().split()))

ab = a*b
ac = a*c
ad = a*d
bc = b*c
bd = b*d
cd = c*d

if ab == cd or ac == bd or ad == bc:
 print('Possible')
else:
 print('Impossible')

