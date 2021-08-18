d, x, y = list(map(float, input().split()))
l = list(map(int, input().split()))
sum1 = d * x
ft = y
st = y - (y * 2) / 100
tt = y - (y * 4) / 100
ftt = y - (y * 6) / 100
fifth = y - (y * 8) / 100
sixth = y - (y * 10) / 100
sum2 = 0
for i in range(len(l)):
    if(l[i] == 6):
        sum2 = sum2 + sixth
    elif(l[i] == 5):
        sum2 = sum2 + fifth
    elif(l[i] == 4):
        sum2 = sum2 + ftt
    elif(l[i] == 3):
        sum2 = sum2 + tt
    elif(l[i] == 2):
        sum2 = sum2 + st
    elif(l[i] == 1):
        sum2 = sum2 + ft
if((sum1 + sum2) >= 300):
    print('YES')
else:
    print('NO')
