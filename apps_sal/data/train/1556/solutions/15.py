try:
    tc=int(input())
    for _ in range(tc):
        n=int(input())
        a=0
        st=""
        for i in range(n):
            if a%2==1:
                st+='0'
            else:
                st+='1'
            a+=1
        for j in range(n):
            print(st)
except:
    pass
