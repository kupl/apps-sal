from sys import stdin, stdout

BitsSetTable256 = [0] * 256


def initialize():
    BitsSetTable256[0] = 0
    for i in range(256):
        BitsSetTable256[i] = (i & 1) + BitsSetTable256[i // 2]


def countSetBits(n):
    return (BitsSetTable256[n & 0xff]
      + BitsSetTable256[(n >> 8) & 0xff]
      + BitsSetTable256[(n >> 16) & 0xff]
            + BitsSetTable256[n >> 24])


initialize()

for _ in range(int(stdin.readline())):
    N, Q = list(map(int, stdin.readline().split(' ')))
    inpList = list(map(int, stdin.readline().split(' ')))
    queryList = []
    resList = []
    even = odd = 0
    for i in inpList:
        temp = 1 ^ i
        setBits = countSetBits(temp)
        if setBits % 2 == 0:
            even += 1
        else:
            odd += 1
    for i in range(Q):
        q = int(stdin.readline())
        setBits = countSetBits(q)
        if setBits % 2 != 0:
            stdout.write("{} {}\n".format(even, odd))
        else:
            stdout.write("{} {}\n".format(odd, even))
