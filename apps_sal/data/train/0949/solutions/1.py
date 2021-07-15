# cook your dish here
try:
    x = int(input())
    for _ in range(x):
        y=int(input())
        a=list(map(int,input().split()))
        if len(list(set(a)))==len(a):
            print(0)
        else:
            j=0
            e=0
            while j<y:
                count=0
                i=j
                while i < len(a):
                    if i+1<y:
                        if a[i]==a[i+1] :
                            i+=1
                            count+=1
                        else:
                            if i+2<y:
                                if a[i]==a[i+2] :
                                    i+=2
                                    count+=1
                                else:    
                                    break
                            else:
                                break
                    else:
                        break
                j=j+1
                e=max(e,count)
            print(e)
except:
    pass
