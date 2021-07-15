from itertools import combinations_with_replacement
find_prime=lambda n:all(n % i for i in range(2, int(n ** .5) + 1)) and n > 1
solve=lambda s,e:len([1for i in combinations_with_replacement([i for i in range(s,e)if find_prime(i)],2)if find_prime(sum(map(int,str(i[0]*i[1]))))])
