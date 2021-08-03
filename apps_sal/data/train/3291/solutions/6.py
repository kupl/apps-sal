import bisect


def primes1(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


lst = primes1(10000)


def primes_a_p(lower_limit, upper_limit):
    lst0 = lst[bisect.bisect_left(lst, lower_limit):bisect.bisect_right(lst, upper_limit)]
    ans = []
    for i in range(len(lst0) - 5):
        for j in range(30, 1500, 30):
            x = lst0[i] + j
            if x not in lst0:
                continue
            if x > lst0[-1]:
                break
            temp = [lst0[i], x]
            flag = True
            while len(temp) < 6:
                x += j
                if x in lst0:
                    temp.append(x)
                else:
                    flag = False
                    break
            if flag == True:
                ans.append(temp)
    return ans
