def solve(n):
    c= 1
    r = list(range(1,n+1))
    for i in r:
        x = ''
        if 3<=i<n:
            x+=str(c)
            c+=1
            for j in range(i-2):
                x+=' '
            x+=str(c)
            c+=1
        else:
            for j in range(i):
                x+=str(c)
                c+=1
        print(x)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        solve(n)


main()

