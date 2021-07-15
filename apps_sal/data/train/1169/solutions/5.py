#!/usr/bin/env python

WORDS = {'F':'FRIENDS',  'L':'LOVE',    'A':'ADORE',
         'M':'MARRIAGE', 'E':'ENEMIES', 'S':'SISTER'}

def process(N1, N2):
    N3 = ''
    for i in range(len(N1)):
        v = N2.find(N1[i])
        if v != -1: N2 = N2[:v] + N2[v+1:]
        else:       N3 = N3 + N1[i]
    N = len(N3 + N2)
    if N == 0: return 'SISTER' # ???
    ar = 'FLAMES'
    stp = 1
    for x in range(6, 1, -1):
        g = ((N%x)+stp)-1
        if g>x:
           g=g%x
        if g==0:
           g=len(ar)
        ar = ar[:g-1] + ar[g:]
        stp=g
    return WORDS[ar]

def main():
    T = int(input())
    for t in range(T):
        N1 = input()
        N2 = input()
        N1 = N1.upper().replace(' ', '') # ???
        N2 = N2.upper().replace(' ', '') # ???
        print(process(N1, N2))

main()

