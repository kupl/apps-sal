has_two_cube_sums=lambda n:sum([(i[0]**3)+(i[1] ** 3)==n for i in __import__("itertools").permutations(range(1,int(n**(1./3.))+1),2)])>=4
