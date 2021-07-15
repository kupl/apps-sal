from collections import defaultdict

def sum_for_list(lst):

    primes = [2,]
    # Use list instaed of int to account for zero sums
    factors_dict = defaultdict(list)
    answer = []

    # Get the needed prime numbers
    x = 3
    for num in range(max(abs(i) for i in lst)):
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primes += [x]
        x += 2
               
    # Dictionary, keys are prime numbers, values are zero
    for k in primes:
        factors_dict[k]

    # Find the prime numbers that are factors of the lst and add to dictionary
    for prime in primes:
        for i in lst:
            if i % prime == 0:
                factors_dict[prime] += [i]

    # Go through dictionary, if no values dont add to answer
    # Sum the values from lst (get those pesky zero sums)
    for k, v in list(factors_dict.items()):
        if v:
            answer += [[k,sum(v)]]

    return answer

