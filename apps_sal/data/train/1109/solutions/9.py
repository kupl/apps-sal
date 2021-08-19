def divisors(n):
    count = 2  # accounts for 'n' and '1'
    i = 2
    while(i**2 < n):
        if(n % i == 0):
            count += 2
        i += 1
    count += (1 if i**2 == n else 0)
    return count


T = int(input())
for t in range(T):
    n = int(input())
    d = divisors(n)
    if d % 2 != 0:
        print("YES")
    else:
        print("NO")
