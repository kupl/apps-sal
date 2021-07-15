def combine(*args):
    result = []
    args_length = len(args)
    max_len_list = max([len(l) for l in args])
    for i in range(max_len_list):
        for j in range(args_length):
            if len(args[j]) > i:
                result.append(args[j][i])
    return result
