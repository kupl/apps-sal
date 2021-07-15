ss = input().split()

N = int ( input() )


print( ss[0] , ss[1] )

for x in range(N):
	
	zz = input().split()
	if ( zz[0] == ss[0] ):
		ss[0] = zz[1]
	else :
		ss[1] = zz[1]
	print( ss[0] , ss[1] )
		


