def opp(a):
    if a=="Right":
        return "Left"
    else:
        return "Right"
def main():
    t=int(input())
    while(t):
        t-=1
        n=int(input())
        a=[]
        for i in range(n):
            a.append(list(_ for _ in input().split(' on ')))
        a.reverse()
        print("Begin on", a[0][1])
        for i in range(1,n):
            print(opp(a[i-1][0]),"on",a[i][1])
        print("")
main()
