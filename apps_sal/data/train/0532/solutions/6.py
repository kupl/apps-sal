
'''def abcd(n):
    x=(1+math.sqrt(5))/2
    y=(1-math.sqrt(5))/2
    
    val=((power(x, n, 15746)-power(y, n, 15746))//math.sqrt(5))
    return(int(val))'''
    
def main():
    n=int(input())
    #x=abcd(n+1)
    a=1;    b=2;
    if(n==1):
        print(1)
    elif(n==2):
        print(2)
    else:
        for i in range(3, n+1):
            temp=(a+b)%15746
            a=b%15746
            b=temp%15746
            
        print(temp%15746)
        #print(power(0.55, 67, 1355))
        
main()
