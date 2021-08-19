# cook your code here
n = input()
x = len(n)
no = list(map(int, n))
temp = [0] * x
if (x > 2):
    sum = 99
    for i in range(3, x):
        sum = sum + 90
    sum = sum + 10 * (int(n[0]) - 1)
    sum = sum + int(n[1])
    f = int(n[0]) % 10

    s = int(n[1]) % 10

    cd = s - f

    temp[0] = n[0]
    temp[1] = n[1]
    for i in range(2, x):
        nxt = (s + cd) % 10
        temp[i] = (chr(nxt + 48))
        s = nxt
    temp = list(map(int, temp))
    if(temp <= no):
        sum = sum + 1
    print(sum)
else:
    print(n)
