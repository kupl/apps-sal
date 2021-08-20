import re
M = [M ** 3 for M in range(1, 2000000) if re.match('[13579]+$', str(M ** 3))]
M = sorted(M + [-M for M in M])


def odd_dig_cubic(Q, S):
    return [V for V in M if Q <= V <= S]
