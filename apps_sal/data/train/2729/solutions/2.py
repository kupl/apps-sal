def find_jane(n):
    return (n-1) // 2
    
"""
1,2,3,...,n
cost = (a+b) % (n+1)

best association is:
    b = n+1-a  ->  cost=0
    
    1 2 3 4 5     -> 1 <-> 5
                     2 <-> 4

to link ("L") those two, the best remaining way is:
    b = n+1-a+1  -> cost=1

    1 2 3 4 5     -> 1 <-> 5: 0
                  L: 5 <-> 2: 1
                     2 <-> 4: 0
                  L: 4 <-> 3: 1
                 --------------
                 total cost = 2


    1 2 3 4       -> 1 <-> 4: 0
                  L: 4 <-> 2: 1
                     2 <-> 3: 0
                 --------------
                 total cost = 1

And so on...
"""
