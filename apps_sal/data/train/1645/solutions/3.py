from collections import Counter
sum_of_squares=lambda n:1 if (n**.5).is_integer() else 2 if all(not j&1 for i, j in Counter(two(n)).items() if i%4==3) else 4 if four(n) else 3

def two(n):
        j, li = 2, []
        while j * j <= n:
            if n % j: j+=1 ; continue 
            li.append(j) ; n //= j 
        return li + [[], [n]][n > 0]
def four(x):
        while x % 4 == 0 : x //= 4
        return 8 * (x // 8) + 7 == x 
