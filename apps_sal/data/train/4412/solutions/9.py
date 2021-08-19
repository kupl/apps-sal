import itertools


def find(n, z):
    find.combination_dict = {0: ((),),
                             1: (((0,),), ), }
    # 2:(((0,), (1,)), ((0, 1),), ), }
    # 3: (((0,), (1,), (2,)), ((0,), (1,2)), ((1,), (0,2)), ((2,), (0,1)), ((0,1,2),),)}

    def get_combination(length):
        if length not in find.combination_dict:
            for i in range(length):
                get_combination(i)
            template = list(range(length))
            result = [{tuple(i for i in template)}]
            for init_tuple_length in range(1, length):
                for c in itertools.combinations(template, init_tuple_length):
                    remain = [i for i in template if i not in c]
                    for combinations in find.combination_dict[length - init_tuple_length]:
                        new_combination = [tuple(c)]
                        for combination in combinations:
                            new_combination.append(tuple(remain[index] for index in combination))
                        if set(new_combination) not in result:
                            result.append(set(new_combination))
            find.combination_dict[length] = tuple(tuple(i) for i in result)
        return find.combination_dict[length]

    def f(num):
        num = str(num)
        value = []
        for combinations in get_combination(len(num)):
            if len(combinations) != 1:
                for combination in combinations:
                    value.append(''.join(num[i] for i in combination))
        return sum(map(int, value))

#     print('running', n, f(n), z)
    limit = f(n) + z
    for nf in itertools.count(n):
        if f(nf) > limit:
            return nf
