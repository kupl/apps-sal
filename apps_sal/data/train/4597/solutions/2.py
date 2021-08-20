def combine(*args):
    res = []
    num_of_args = len(args)
    len_of_longest_list = max([len(l) for l in args])
    for i in range(len_of_longest_list):
        for j in range(num_of_args):
            if len(args[j]) > i:
                res.append(args[j][i])
    return res
