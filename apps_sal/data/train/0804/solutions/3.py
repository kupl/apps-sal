# cook your dish here
import numpy as np
tests = int(input())
for _ in range(tests):
    n = int(input()) - 1
    soldiers = [int(j) for j in input().split()]
    force = int(input())
    attacks = np.zeros(2 * n, dtype=int)
    attacks[:n] = np.array(soldiers)
    attacks[n:2 * n] = attacks[:n]
    shield = [0 for _ in range(n)]
    for i in range(n):
        if attacks[i] > force:
            shield[i] = 10 ** 11
        else:
            shield[i] = force
            num_of_survivors = n
            soldiers = list(attacks[i:i + n])
            starting_soldier = (n - i) % n
            while num_of_survivors > 1:
                if (num_of_survivors - starting_soldier) % 2 == 1:
                    shield[i] += soldiers[-1]
                soldiers = [soldiers[i] for i in range(num_of_survivors) if i < starting_soldier or (i - starting_soldier) % 2 == 0]
                num_of_survivors = starting_soldier + (num_of_survivors - starting_soldier + 1) // 2
                starting_soldier = 0
    shield_needed = min(shield)
    if shield_needed == 10 ** 11:
        print("impossible")
    else:
        print("possible")
        for i in range(n):
            if shield[i] == shield_needed:
                print(str(i + 1) + " " + str(shield_needed))
                break
