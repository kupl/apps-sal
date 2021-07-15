
def digitSum(digit):
    result=0
    s=str(digit)
    for x in s:
        result+=int(x)
    return result

def main():
    t=int(input())
    for _ in range(t):
        l=[]
        min1, pos=100000, -10
        # f=[]
        # craw=[True, False, False, False, False, False, False, False, False, False]
        # dic={}
        # fag=[True]*10
        n, d=input().split(" ")
        n=int(n)
        d=int(d)

        i=0
        # if d%9==0:
        #     i=0
        #     while n>9:
        #         i+=1
        #         n=digitSum(n)
        #     print(n, i, sep=" ")
        # elif d%3==0:
        #     i=0
        #     while n>3:
        #         i+=1
        #         if n>9:
        #             n=digitSum(n)
        #         else:
        #             n+=d
        #     print(n, i, sep=" ")
        # else:
        l.append([n, 0])
        while i<10000 and l:
            tem=l.pop(0)
            if min1>tem[0]:
                min1=tem[0]
                pos=tem[1]
            if tem[0]>9:
                l.append([digitSum(tem[0]), tem[1]+1])
            l.append([tem[0]+d, tem[1]+1])
            i+=1
        print("{0} {1}".format(min1, pos))
main()
