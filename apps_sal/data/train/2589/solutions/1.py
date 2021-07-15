#!/usr/bin/env python3

def __starting_point():
    t = int(input().strip())
    
    for _ in range(t):
        a, b = input().strip().split(' ')
        
        try:
            print((int(a)//int(b)))
        except ZeroDivisionError as e:
            print(("Error Code: {}".format(e)))
        except ValueError as e:
            print(("Error Code: {}".format(e)))

__starting_point()
