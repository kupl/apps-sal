def prime(n):
    nroot = int(n ** 0.5) + 1
    ctr = 0
    seive = [2, 3, 5, 7, 11, 13]
    if n <= seive[-1]:
        return seive
    else:
        n_start = seive[-1] + 1
        for i in range(n_start, n):
            iroot = int(i ** 0.5) + 1
            for j in seive:
                if i % j == 0:
                    ctr = 0
                    break
                elif j > iroot:
                    ctr = 1
                    break
            if ctr == 1:
                seive.append(i)
        return seive


seive = prime(81100)
t = int(input())
for l in range(t):
    n = int(input())
    s = []
    sump = 0
    for i in range(n):
        j = seive[i]
        sump = (sump + seive[j - 1] % 1000000007) % 100000000
    print(sump)
