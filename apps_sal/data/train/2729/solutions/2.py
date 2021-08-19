def find_jane(n):
    return (n - 1) // 2


'\n1,2,3,...,n\ncost = (a+b) % (n+1)\n\nbest association is:\n    b = n+1-a  ->  cost=0\n    \n    1 2 3 4 5     -> 1 <-> 5\n                     2 <-> 4\n\nto link ("L") those two, the best remaining way is:\n    b = n+1-a+1  -> cost=1\n\n    1 2 3 4 5     -> 1 <-> 5: 0\n                  L: 5 <-> 2: 1\n                     2 <-> 4: 0\n                  L: 4 <-> 3: 1\n                 --------------\n                 total cost = 2\n\n\n    1 2 3 4       -> 1 <-> 4: 0\n                  L: 4 <-> 2: 1\n                     2 <-> 3: 0\n                 --------------\n                 total cost = 1\n\nAnd so on...\n'
