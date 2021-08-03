t = int(input())
x = 'abcdefghijklmnopqrstuvwxyz'
for i in range(t):
    a = 0
    b = input().split()
    c = input()
    for j in range(len(x)):
        if(x[j] not in c):
            a = a + int(b[j])
    print(a)
