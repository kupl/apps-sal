import math


def seq_len_formula(s, b, n, i):
    return s + i * b + n * (i * (i + 1) // 2)


def increasing_step(num_len, block_len, seq_len):
    num_of_blocks = 9 * 10 ** num_len
    num_len += 1
    seq_len = seq_len_formula(seq_len, block_len, num_len, num_of_blocks)
    block_len = block_len + num_len * num_of_blocks
    return (num_len, block_len, seq_len)


def solve(n):
    buffer = IS_seq_len = (0, 0, 0)
    while IS_seq_len[2] < n:
        (num_len, block_len, seq_len) = buffer = IS_seq_len
        IS_seq_len = increasing_step(num_len, block_len, seq_len)
    (num_len, init_block_len, init_seq_len) = buffer
    step = 9 * 10 ** num_len
    num_len += 1
    buffer = (0, init_seq_len)
    while step > 0:
        (num_of_blocks, seq_len) = buffer
        while seq_len < n:
            buffer = (num_of_blocks, seq_len)
            num_of_blocks += step
            seq_len = seq_len_formula(init_seq_len, init_block_len, num_len, num_of_blocks)
        step = round(step / 10)
    n -= buffer[1]
    buffer = IS_block_len = (0, 0, 0)
    while IS_block_len[1] < n:
        (num_len, block_len, seq_len) = buffer = IS_block_len
        IS_block_len = increasing_step(num_len, block_len, seq_len)
    num_len = 10 ** buffer[0] - 1
    block_len = buffer[1]
    amount_of_nums = math.ceil((n - block_len) / len(str(num_len + 1)))
    n = n - amount_of_nums * len(str(num_len + 1)) - block_len - 1
    num = amount_of_nums + num_len
    return int(str(num)[n])
