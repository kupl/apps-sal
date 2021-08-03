def factors(x):
    if type(x) == str or x < 1 or type(x) == float:
        return -1

    else:
        divisor = list(range(1, x + 1))
        ans = []
        for i in divisor:
            if x % i == 0:
                ans.append(i)
                ans.sort(reverse=True)
        return ans
