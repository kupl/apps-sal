check=int(input())+1
while(check<=987654321) :
    val=str(check)
    temp=set(val)
    if len(temp)==len(val) and '0' not in temp :
        break
    else :
        check+=1
if check<=987654321 :
    print(check)
else :
    print(0)
