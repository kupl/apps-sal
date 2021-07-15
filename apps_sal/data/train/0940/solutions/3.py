T = eval(input())
t = int(T)
C = []
for i in range(t):
    c = eval(input())
    C.append(c)


def max():
    for i in range(t):
        m = 2*int(C[i])*int(C[i])
        print(m)


max()       
    

