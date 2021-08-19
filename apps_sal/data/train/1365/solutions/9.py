import random
import time


def get_input():
    inp_str = input()
    return inp_str


def get_nth_fibbo(n):
    a = 0
    b = 1
    while n > 0:
        (a, b) = (b, a + b)
        n -= 1
    return b


def count_unique(inp_str):
    unique_count = 1
    if 'c' in inp_str or 'x' in inp_str:
        return 0
    count_arr = []
    cur_chr = None
    cur_chr_len = 0
    for char in inp_str:
        if cur_chr is None:
            cur_chr = char
            cur_chr_len = 1
            continue
        if char == cur_chr:
            cur_chr_len += 1
        else:
            if cur_chr in ['f', 'g']:
                count_arr.append(cur_chr_len)
            cur_chr = char
            cur_chr_len = 1
    if cur_chr in ['f', 'g']:
        count_arr.append(cur_chr_len)
    for count in count_arr:
        unique_count *= get_nth_fibbo(count)
    return unique_count


def test():
    n = random.randint(5, 10)
    ord_a = ord('e')
    ord_z = ord('h') + 1
    inp_str = ''.join([chr(random.randrange(ord_a, ord_z)) for _ in range(n)])
    unique_count = count_unique(inp_str) % (10 ** 9 + 7)
    if unique_count > 10:
        print('Input: {}'.format(inp_str))
        print('Unique: {}'.format(unique_count))
        time.sleep(2)


def stress_test():
    while True:
        test()


def main():
    inp_str = get_input()
    r = count_unique(inp_str) % (10 ** 9 + 7)
    print(r)


def __starting_point():
    main()


'\nfffff\ncfff\nccf\ncfc\nfcff\nfcc\nffcf\nfffc\n\n'
__starting_point()
