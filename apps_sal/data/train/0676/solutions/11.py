# cook your dish here
T=int(input())
if T<1 or T>100:
        print("Exceeded testcases limit")
        return
sum=0
for i in range (0,T):
    N=int(input())
    if N<1 or N>100000:
        print("Exceeded number of girls limit")
        return
    string=input()
    S=string.split()
    L=[]
    for i in S:

        if len(i)<1 or len(i)>10:
            print("Exceeded string length limit")
            return
        L.append(i.lower())
    sum+=N
    if sum>1000000:
        print("Exceeded Sum of N over all the test cases limit")
        return
    lcount=[]
    newlist=[]
    for i in L:
        if i not in newlist:
            newlist.append(i)
            freq=L.count(i)
            lcount.append(freq)
    maximum=max(lcount)
    mostliked=[]
    for i in range (0,len(lcount)):
        if lcount[i]==maximum:
            mostliked.append(newlist[i])
    mostliked.sort()
    print(mostliked[0])
