import sys


def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))


INF = float('inf')

n = get_int()
arr = get_array()

curr_nest = 0
max_nest = 1
nest_pos = 0

curr_symbols = 0
max_symbols = 2
max_symbols_open_pos = 0

seq = 0

for ind in range(n):

    curr_symbols += 1

    if arr[ind] == 1:
        seq += 1
        if seq > max_nest:
            max_nest = seq
            nest_pos = ind

    else:
        seq -= 1
        if seq == 0:
            if curr_symbols > max_symbols:
                max_symbols = curr_symbols
                max_symbols_open_pos = ind - curr_symbols + 1
            curr_symbols = 0

print(max_nest, nest_pos + 1, max_symbols, max_symbols_open_pos + 1)
