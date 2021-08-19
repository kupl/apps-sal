def super_size(n):
    num = [int(x) for x in str(n)]  # convert to list
    num.sort(reverse=True)  # sort descending
    num_str = [str(x) for x in num]  # convert list ints to strs, there's got to be a less stupid way
    big_num_str = "".join(num_str)  # join into a integer
    return int(big_num_str)
