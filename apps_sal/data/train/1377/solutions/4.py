# cook your dish her
for _ in range(int(input())):
    l=list(map(int,input().split()))
#print(l)
    avg=((l[0]-l[2])+(l[1]-l[3]))/2
    if(avg>0):
        print(str(avg)+" DEGREE(S) ABOVE NORMAL")
    else:
        print(str(avg*-1)+" DEGREE(S) BELOW NORMAL")
