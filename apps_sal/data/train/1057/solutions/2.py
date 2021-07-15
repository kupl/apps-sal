t=int(input())
for i in range(t):
    number=int(input())
    if '4' not in (str(number)):
        x=len(str(number))+1
        print('4'*x)
    elif number%2==0:
        print(number+3)
    else:
        number=str(number)
        for i in range(len(number)-1,-1,-1):
            if number[i]=='4':
                index=i
                break
        q=int(index)
        u=number[0:q]
        lennew=len(number)-(index+1)
        print(u+'7'+'4'*lennew)
      


