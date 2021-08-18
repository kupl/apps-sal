import sys
def fop(s): sys.stdout.write(str(s) + '\n')
def fip(): return sys.stdin.readline()


def fintinp(): return int(fip())
def flistinp(func=int): return list(map(func, fip().split()))
def fnsepline(n, func=str): return [func(fip()) for _ in range(n)]


def even(x):
    x = bin(x).count('1')
    return x % 2 == 0


for _ in range(fintinp()):
    q = fintinp()
    o = e = 0
    nums = set()
    for qn in range(q):
        qn = fintinp()
        if qn not in nums:
            if even(qn):
                e += 1
            else:
                o += 1

            for n in set(nums):
                x = n ^ qn
                if x not in nums:
                    if even(x):
                        e += 1
                    else:
                        o += 1

                    nums.add(x)

        nums.add(qn)
        print(e, o)
