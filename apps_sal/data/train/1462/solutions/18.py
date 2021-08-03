#import logging
#import sys
#sys.stdin = open("input.txt", "r")
#sys.stdout = open("output.txt", "w")
#logging.basicConfig(filename="test.log", level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
t = int(input())
while t:
    t -= 1
    s = input()
    s = s.upper()
    if s.find('BERHAMPORE') != -1 and s.find('SERAMPORE') != -1:
        print("Both")
        continue
    if s.find('BERHAMPORE') != -1:
        print("GCETTB")
        continue
    elif s.find('SERAMPORE') != -1:
        print("GCETTS")
        continue
    else:
        print("Others")
