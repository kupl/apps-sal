
import sys


def solve(r, w):
    """
    :param r:
    :param w:
    :return:
    """
    data = r.readline().split()
    num_elems = int(data[0])
    num_ops = int(data[1])
    num_queries = int(data[2])

    elem_list = [int(x) for x in r.readline().split()]
    a = [0] * (num_ops + 1)
    b = [0] * (num_elems + 1)

    op_list = []
    for _ in range(num_ops):
        op_list.append(tuple([int(x) for x in r.readline().split()]))

    for _ in range(num_queries):
        query = [int(x) for x in r.readline().split()]
        a[query[0] - 1] += 1
        a[query[1]] -= 1

    c = 0
    for i, cur_op in enumerate(op_list):
        cur_op = op_list[i]
        c += a[i]
        b[cur_op[0] - 1] += c * cur_op[2]
        b[cur_op[1]] -= c * cur_op[2]

    c = 0
    for i, elem in enumerate(elem_list):
        c += b[i]
        print(elem + c, end=' ')


def __starting_point():
    solve(sys.stdin, sys.stdout)


__starting_point()
