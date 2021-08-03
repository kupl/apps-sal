def presses(s): return sum((c in b) * (1 + b.find(c)) for c in s.lower() for b in
                           '1,abc2,def3,ghi4,jkl5,mno6,pqrs7,tuv8,wxyz9,*, 0,#'.split(","))
