import fractions
for i in range(eval(input())):
 n,z=eval(input()),list(map(int,input().split()))
 q=z[0]
 for __ in range(1,n): q=fractions.gcd(q,z[__])
 print(q*n)

