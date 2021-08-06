import atexit
import io
import sys
import math
from collections import defaultdict, Counter

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# sys.stdout=open("CP2/output.txt",'w')
# sys.stdin=open("CP2/input.txt",'r')

# m=pow(10,9)+7
t = int(input())
for i in range(t):
    m, c, h = map(int, input().split())
    if (h - c) % 3 == 0 and (h - c) // 3 <= m:
        print("No")
    else:
        print("Yes")
