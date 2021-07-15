t=int(input())
for i in range(t):
    str1=input()
    str1=str1[::-1]
    ans=0
    for j in range(len(str1)):
        if(str1[j]=="0" or str1[j]=="1" or str1[j]=="2" or str1[j]=="3" or str1[j]=="4" or str1[j]=="5" or str1[j]=="6" or str1[j]=="7" or str1[j]=="8" or str1[j]=="9"):
            ans+=int(str1[j])*(16**j)
        elif(str1[j]=="A"):
            ans+=10*(16**j)
        elif(str1[j]=="B"):
            ans+=11*(16**j)
        elif(str1[j]=="C"):
            ans+=12*(16**j)
        elif(str1[j]=="D"):
            ans+=13*(16**j)
        elif(str1[j]=="E"):
            ans+=14*(16**j)
        elif(str1[j]=="F"):
            ans+=15*(16**j)
    print(ans)
