def fun(x,y):
    if x==y:
        return x
    if (y&(y+1)) == 0:
        return y
    [a,b] = [len(bin(x))-3,len(bin(y))-3]
    if a==b:
        return (1<<a)| fun((1<<a)^x, (1<<a)^y)
    return (1<<b) - 1
    
def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    [n]=get()
    for z in range(n):
        [x,y]=get()
        print(fun(x,y))


    if mode=="file":f.close()


def __starting_point():
    main()

__starting_point()
