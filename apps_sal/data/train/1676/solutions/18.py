import sys
mp=[[0 for i in range(10)] for j in range(10)]
an=[0,0]
x=[]
y=[]
def smx(index):
    if index==1:
        y=[0]
    elif index==2:
        y=[0,1]
    elif index==3:
        y=[0,0]
    elif index==4:
        y=[0,1,2]
    elif index==5:
        y=[0,0,0]
    elif index==6:
        y=[0,1,2,3]
    elif index==7:
        y=[0,0,0,0]
    elif index==8:
        y=[0,1,2,3,4]
    elif index==9:
        y=[0,0,0,0,0]
    elif index==10:
        y=[0,1,0,1]
    elif index==11:
        y=[0,1,2,0,1,2,0,1,2]
    elif index==12:
        y=[0,0,0,1,2]
    elif index==13:
        y=[2,2,0,1,2]
    elif index==14:
        y=[0,1,2,2,2]
    elif index==15:
        y=[0,1,2,0,0]
    elif index==16:
        y=[0,1,0]
    elif index==17:
        y=[0,0,1]
    elif index==18:
        y=[1,0,1]
    elif index==19:
        y=[0,1,1]
    return max(y)
def chk():
    for i in range(10):
        if sum(mp[i])==10:
            for j in range(10):
                mp[i][j]=0
    for j in range(10):
        flag=1
        for i in range(10):
            if mp[i][j]==0:
                flag=0
                break
        if flag==1:
            for i in range(10):
                mp[i][j]=0
def fil(y,x):
    for i1 in range(len(x)):
        if an[0]+x[i1]<10 and an[1]+y[i1]<10:
            mp[an[0]+x[i1]][an[1]+y[i1]]=1
    #chk()
def ind(y,x):
    for i in range(10):
        for j in range(10):
            flag=1
            for i1 in range(len(x)):
                if i+x[i1]<10 and j+y[i1]<10 and mp[i+x[i1]][j+y[i1]]!=0:
                    flag=-1
                    break
                if i+x[i1]>=10 or j+y[i1]>=10:
                    flag=-1
                    break
            if flag==1:
                an[0]=i
                an[1]=j
                return True
    return False
def find(index):
    if index==1:
        x=[0]
        y=[0]
    elif index==2:
        x=[0,0]
        y=[0,1]
    elif index==3:
        x=[0,1]
        y=[0,0]
    elif index==4:
        x=[0,0,0]
        y=[0,1,2]
    elif index==5:
        x=[0,1,2]
        y=[0,0,0]
    elif index==6:
        x=[0,0,0,0]
        y=[0,1,2,3]
    elif index==7:
        x=[0,1,2,3]
        y=[0,0,0,0]
    elif index==8:
        x=[0,0,0,0,0]
        y=[0,1,2,3,4]
    elif index==9:
        x=[0,1,2,3,4]
        y=[0,0,0,0,0]
    elif index==10:
        x=[0,0,1,1]
        y=[0,1,0,1]
    elif index==11:
        x=[0,0,0,1,1,1,2,2,2]
        y=[0,1,2,0,1,2,0,1,2]
    elif index==12:
        x=[0,1,2,2,2]
        y=[0,0,0,1,2]
    elif index==13:
        x=[0,1,2,2,2]
        y=[2,2,0,1,2]
    elif index==14:
        x=[0,0,0,1,2]
        y=[0,1,2,2,2]
    elif index==15:
        x=[0,0,0,1,2]
        y=[0,1,2,0,0]
    elif index==16:
        x=[0,0,1]
        y=[0,1,0]
    elif index==17:
        x=[0,1,1]
        y=[0,0,1]
    elif index==18:
        x=[0,1,1]
        y=[1,0,1]
    elif index==19:
        x=[0,0,1]
        y=[0,1,1]
    if ind(x,y):
        fil(x,y)
        return True
    return False
a,b,c=list(map(int,input().split()))
while(a!=-1):
    ans=""
    flag=0
    if find(a):
       ans+="1 "+ str(an[0]+1+smx(a))+" "+str(an[1]+1)+" "
    else:
        flag+=1
    if find(b):
       ans+="2 "+ str(an[0]+1+smx(b))+" "+str(an[1]+1)+" "
    else:
        flag+=1
    if find(c):
       ans+="3 "+ str(an[0]+1+smx(c))+" "+str(an[1]+1)+" "
    else:
        flag+=1
    while(flag>0):
        ans+="-1 -1 -1 "
        flag-=1
    print(ans)
    sys.stdout.flush()
    a,b,c=list(map(int,input().split()))

