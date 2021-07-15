import math

def seq_len_formula(s, b, n, i): return s + i * b + n * (i * (i + 1) // 2)

def point_gen():
    num_len, block_len, seq_len = 0, 0, 0
    while True:
        yield num_len, block_len, seq_len
        num_of_blocks = 9 * 10 ** num_len
        num_len += 1
        seq_len = seq_len_formula(seq_len, block_len, num_len, num_of_blocks)
        block_len = block_len + num_len * num_of_blocks
        
def linear_search(index, parameter):
    params = {'block_len': 1, 'seq_len': 2}
    required_point = 0, 0, 0
    for point in point_gen():
        if point[params[parameter]] >= index: return required_point
        required_point = point

def index_for_block(num_len, block_len, index):
    corrector = num_of_blocks = 9 * 10 ** (num_len - 1)
    seq_len = seq_len_formula(0, block_len, num_len, num_of_blocks)
    while not seq_len < index <= seq_len_formula(0, block_len, num_len, num_of_blocks + 1):
        corrector = math.ceil(corrector / 2)
        num_of_blocks = num_of_blocks - corrector if seq_len >= index else num_of_blocks + corrector
        seq_len = seq_len_formula(0, block_len, num_len, num_of_blocks)
    return index - seq_len

def solve(index):
    initial_len, initial_block_len, initial_seq_len = linear_search(index, 'seq_len')
    index = index_for_block(initial_len + 1, initial_block_len, index - initial_seq_len)
    buffer = linear_search(index, 'block_len')
    num_len, block_len = 10 ** buffer[0] - 1, buffer[1]
    amount_of_nums = math.ceil((index - block_len) / len(str(num_len + 1)))
    return int(str(amount_of_nums + num_len)[index - amount_of_nums * len(str(num_len + 1)) - block_len - 1])
