import sys
import math
def Int(): return int(input())
def Str(): return input()
def Ints(): return list(map(int, input().split(" ")))
def int_arr(): return list(map(int, input().strip().split(" ")))
def str_arr(): return list(map(str, input().split(" ")))


def vsInput():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


no_of_books = Int()
books = int_arr()
no_aken = Int()
for i in range(no_aken):
    position = Int()
    print(books[position - 1])
    books.pop(position - 1)
