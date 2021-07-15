def solve(a,b):
    for char in b:
        return 0 if b.count(char) > a.count(char) or len(b)>=len(a) else len(a)-len(b) 

