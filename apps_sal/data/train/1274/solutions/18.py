try:
    t = int(input())
    for a in range(t):
        k = int(input())
        for i in range(1,k+1):
            s = ""
            x = 1
            for j in range(1,(2*k)+1):
                if (j%2==0):
                    s+=str(i)
                else:
                    s+=str(x)
                    x+=1
            print(s)

except EOFError:
    pass
