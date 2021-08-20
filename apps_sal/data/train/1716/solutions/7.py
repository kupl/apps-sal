import itertools as it
import copy
operator = ['+', '-', '*', '/']


def gnrt_exp(a, b):
    return ['({0})*({1})'.format(a, b), '({0})/({1})'.format(a, b), '({0})/({1})'.format(b, a), '({0})+({1})'.format(a, b), '({0})-({1})'.format(a, b), '({0})-({1})'.format(b, a)]


def equal_to_24(a, b, c, d):
    List = [a, b, c, d]
    for (fst, scnd) in it.combinations(List, 2):
        temp = copy.deepcopy(List)
        temp.remove(fst)
        temp.remove(scnd)
        for exp1 in gnrt_exp(fst, scnd):
            for thrd in it.combinations(temp, 1):
                temp1 = copy.deepcopy(temp)
                temp1.remove(thrd[0])
                for exp2 in gnrt_exp(exp1, thrd[0]):
                    for exp3 in gnrt_exp(exp2, temp1[0]):
                        try:
                            rst_final = eval(exp3)
                        except:
                            rst_final = 0
                        if rst_final == 24:
                            return exp3
    for (fst, scnd) in it.combinations(List, 2):
        temp = copy.deepcopy(List)
        temp.remove(fst)
        temp.remove(scnd)
        for exp1 in gnrt_exp(fst, scnd):
            for exp2 in gnrt_exp(*temp):
                for exp in gnrt_exp(exp1, exp2):
                    print(exp)
                    try:
                        rst_final = eval(exp)
                    except:
                        rst_final = 0
                    if rst_final == 24:
                        return exp
    return "It's not possible!"
