n = int(input())
x = input()
y = input()
xl = [int(i) for i in x]
yl = [int(i) for i in y]
c1 = 0
c2 = 0
cnt1 = xl.count(1)
cnt0 = xl.count(0)
# print(cnt1)
for i in range(n):
    if(x[i] == '0' and y[i] == '0'):
        c1 += 1
    elif(x[i] == '1' and y[i] == '0'):
        c2 += 1
cnt1 -= c2
# print(c1,c2)
print(c1 * cnt1 + c2 * cnt0)
