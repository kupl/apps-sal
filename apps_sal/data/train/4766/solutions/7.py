from math import sqrt


def n_closestPairs_tonum(num, k):
    bound = int(sqrt(num * 2 - 1))
    odd_sol = []
    even_sol = []
    if bound % 2 == 1:
        A_square_odd = [i * i for i in list(range(1, bound + 1, 2))[::-1]]
        A_square_even = [i * i for i in list(range(2, bound, 2))[::-1]]
    else:
        A_square_odd = [i * i for i in list(range(1, bound, 2))[::-1]]
        A_square_even = [i * i for i in list(range(2, bound + 1, 2))[::-1]]
    for A_square in A_square_odd:
        for B_square in A_square_odd:
            if len(odd_sol) == num // 2:
                break
            if (A_square + B_square) // 2 < num and (A_square - B_square) // 2 > 0:
                odd_sol.append([(A_square + B_square) // 2, (A_square - B_square) // 2])
        if len(odd_sol) == num // 2:
            break
    for A_square in A_square_even:
        for B_square in A_square_even:
            if len(even_sol) == num // 2:
                break
            if (A_square + B_square) // 2 < num and (A_square - B_square) // 2 > 0:
                even_sol.append([(A_square + B_square) // 2, (A_square - B_square) // 2])
        if len(even_sol) == num // 2:
            break

    ans_li = odd_sol + even_sol
    ans_li.sort(reverse=True)
    return ans_li[:k]
