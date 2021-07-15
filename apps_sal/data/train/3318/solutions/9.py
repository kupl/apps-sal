number_of_carries=r=lambda a,b,c=0:a+b+c and c+r(a//10,b//10,a%10+b%10+c>9)
