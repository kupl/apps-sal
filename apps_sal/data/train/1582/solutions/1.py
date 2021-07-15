# cook your dish here

n=int(input())
string1=input()
count=0
if(n==1):
    print(0)
else:
    for i in range(len(string1)-1):
        if(string1[i+1]==string1[i]):
            count+=1
            
    print(count)
