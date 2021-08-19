class SierpinskiSumFunc:

    def __init__(self):
        sierpinski_number = 4
        sierpinski_numbers_add = (5, 47, 5, 8)
        sierpinski_sum = [4]
        n = 0
        while sierpinski_sum[-1] < 520000000000000:
            sierpinski_number += sierpinski_numbers_add[n]
            sierpinski_sum.append(sierpinski_sum[-1] + sierpinski_number)
            n = 0 if n == 3 else n + 1
        self.sierpinski_sum = tuple(sierpinski_sum)


sierpinski_sum_obj = SierpinskiSumFunc()


def find_closest_value(m):
    if m <= 4:
        return 4
    if m <= 100000:
        sierpinski_sum = sierpinski_sum_obj.sierpinski_sum
        nn = 0
        while True:
            if m == sierpinski_sum[nn]:
                return m
            elif m < sierpinski_sum[nn + 1] and m > sierpinski_sum[nn]:
                return sierpinski_sum[nn + 1] if m - sierpinski_sum[nn + 1] >= sierpinski_sum[nn] - m else sierpinski_sum[nn]
            nn += 1
    elif m > 100000:
        sierpinski_sum = sierpinski_sum_obj.sierpinski_sum
        nn = -1
        while True:
            if m == sierpinski_sum[nn]:
                return m
            elif m > sierpinski_sum[nn - 1] and m < sierpinski_sum[nn]:
                return sierpinski_sum[nn - 1] if m - sierpinski_sum[nn - 1] < sierpinski_sum[nn] - m else sierpinski_sum[nn]
            if m < sierpinski_sum[nn - 20]:
                nn -= 20
            else:
                nn -= 1
