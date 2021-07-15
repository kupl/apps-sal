import sys
def main():
    case=1
    while True:
        try:
            m, n = list(map(int, sys.stdin.readline().split()))
            if m>n:
                m,n=n,m
            r=[str(num) for num in range(m, n+1)]
            s=''.join(r)
            d={}
            for number in s:
                if number not in d:
                    d[number]=1
                else: d[number]+=1
            for q in range(10):
                if str(q) not in d:
                        d[str(q)]=0
            print("Case "+str(case)+": "+"0:"+str(d['0'])+" "+"1:"+str(d['1'])+" "+"2:"+str(d['2'])+" "+"3:"+str(d['3'])+" "+"4:"+str(d['4'])+" "+"5:"+str(d['5'])+" "+"6:"+str(d['6'])+" "+"7:"+str(d['7'])+" "+"8:"+str(d['8'])+" "+"9:"+str(d['9']))
            case+=1
        except:
            break
def __starting_point():
    main()

__starting_point()
