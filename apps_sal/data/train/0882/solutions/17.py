# cook your dish here
from sys import stdin, stdout

try:
    t = eval(stdin.readline())
    for _ in range(t):
        s1 = str(input())
        s2 = str(input())
        
        Dict1 = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,
                'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0,
                'u':0, 'v':0, 'w':0 , 'x':0, 'y':0, 'z':0, 'A': 0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
                'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0,
                'U':0, 'V':0, 'W':0 , 'X':0, 'Y':0, 'Z':0,'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '0':0 }
        Dict2 = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,
                'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0,
                'u':0, 'v':0, 'w':0 , 'x':0, 'y':0, 'z':0, 'A': 0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
                'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0,
                'U':0, 'V':0, 'W':0 , 'X':0, 'Y':0, 'Z':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '0':0 }
        
        answer = 0
        
        for i in range(len(s1)):
            Dict1[s1[i]] += 1
        
        for i in range(len(s2)):
            Dict2[s2[i]] += 1
            
        freqA = list(Dict1.values())
        freqB = list(Dict2.values())

        for j in range(len(Dict1)):
            answer += min(freqA[j], freqB[j])
            
        stdout.write(str(answer) + '\n')            
         
        
except: pass
