from typing import List


def max_tri_sum(numbers: List[int]) -> int:
    m1, m2, m3 = sorted(numbers[:3])
    
    for n in numbers[3:]:
        if n > m1:
            if n > m2:
                if n > m3:
                    m1, m2, m3 = m2, m3, n
                elif n != m3:
                    m1, m2 = m2, n
            elif n != m2:
                m1 = n

    return m1 + m2 + m3

