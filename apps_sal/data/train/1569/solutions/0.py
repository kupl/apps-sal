# cook your dish here
from collections import defaultdict
import sys
import math
from collections import Counter
from collections import OrderedDict


def inputt():
    return sys.stdin.readline().strip()


def printt(n):
    sys.stdout.write(str(n) + '\n')


def listt():
    return [int(i) for i in inputt().split()]


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def find_sub_string(str):
    str_len = len(str)

    # Count all distinct characters.
    dist_count_char = len(set([x for x in str]))

    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0)
    for i in range(str_len):
        curr_count[str[i]] += 1

        if curr_count[str[i]] == 1:
            ctr += 1

        if ctr == dist_count_char:
            while curr_count[str[start_pos]] > 1:
                if curr_count[str[start_pos]] > 1:
                    curr_count[str[start_pos]] -= 1
                start_pos += 1

            len_window = i - start_pos + 1
            if min_len > len_window:
                min_len = len_window
                start_pos_index = start_pos
    return str[start_pos_index: start_pos_index + min_len]


t = int(inputt())
for _ in range(t):
    j = []
    str1 = inputt()
    s = find_sub_string(str1)
    for i in s:
        j.append(abs(97 - ord(i)) + 1)
    st = [str(i) for i in j]
    print(''.join(st))
