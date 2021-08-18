def prime_maxlength_chain(val_max):

    primes = []
    sieve = [1] * (val_max + 1)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, (val_max + 1)):
        if sieve[i] == 0:
            continue
        for j in range(i * i, (val_max + 1), i):
            sieve[j] = 0

    for i in range(val_max + 1):
        if sieve[i] == 1:
            primes.append(i)

    for j in range(400, -1, -1):

        answer = []
        acc = 0
        if len(primes) < j:
            continue

        for i in range(j):
            acc += primes[i]

        if acc <= val_max and sieve[acc] == 1:
            answer.append(acc)

        for i in range(j, len(primes)):
            acc += primes[i]
            acc -= primes[i - j]
            if acc >= val_max:
                break
            if acc <= val_max and sieve[acc] == 1:
                answer.append(acc)
        if len(answer) > 0:
            return answer
