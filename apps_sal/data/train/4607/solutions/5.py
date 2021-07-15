from itertools import permutations
def find_mult_3(num):
    # your code here
    st=str(num)
    val=[ int("".join(i)) for j in range(1,len(st)+1) for i in set(permutations(st,j)) if int("".join(i))>0 and int("".join(i))%3==0  ]
    return [len(set(val)),max(val)]
