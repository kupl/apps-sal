test = eval(input())
for i in range(test):
    powOf5 = 762939453125
    coeff = 200000000000000000
    sum_ = 0
    x = eval(input())
    while x > 25:
        if x % powOf5:
            sum_ += x / powOf5 * coeff
            x %= powOf5
            powOf5 /= 5
        else:
            sum_ += coeff * ((x - 1) / powOf5)
            x = powOf5
            powOf5 /= 5
        coeff /= 10
    mod = x % 5
    if mod == 0:
        mod = 5
    sum_ += (x - mod) * 4 + (mod - 1) * 2
    print(sum_)
