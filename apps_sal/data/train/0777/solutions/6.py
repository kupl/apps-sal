from decimal import Decimal
for _ in range(0,eval(input())):
    [r1,h1,r2,h2],p=list(map(Decimal,input().split())),Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603)
    print(p*(r1**2)*(h1+Decimal(2.0)*r1)/3, p*(r2**2)*h2)
