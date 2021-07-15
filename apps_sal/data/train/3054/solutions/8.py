sum_of_n = lambda n: [0]+[sum(range(i+1))*(n/abs(n)) for i in range(1,abs(n)+1)]
