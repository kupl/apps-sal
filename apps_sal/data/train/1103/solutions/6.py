import fractions


def repeat_factor(n):
    fs = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            q = n / i
            if q % i == 0:
                return i
    return 1


nprobs = int(input())
for i in range(nprobs):
    x = input()
    prob = list(map(int, input().split()))
    found = False
    # for i in range(len(prob)):
    #     for j in range(len(prob)):
    #         if (i != j):
    #             hcf = fractions.gcd(prob[i], prob[j])
    #             if hcf > 1:
    #                 print hcf
    #                 found = True
    #                 break
    #     if found:
    #         break
    # if found:
    #     break
    prod = 1
    for i in prob:
        prod *= i
    # for i in prob:
    #     x = repeat_factor(i)
    #     if x > 1:
    #         print x
    #         break
    x = repeat_factor(prod)
    print(x)
