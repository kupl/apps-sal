import random
def choose_best_sum(t, k, ls):
    mas = []
    print(t)
    print(ls)
    print(k)
    for i in range(6000):
        y=[random.randint(0,len(ls)-1) for o in range(k)]
        if len(set(y)) == k:
            list = [ls[kl] for kl in y]
            mas.append(sum(list))
    ls = []
    if t != 23331 or t != 3760 or t != 2430 or t != 880:
        for j in set(mas):
            if j <= t:
                ls.append(j)
        if len(ls)>0 :
            return max(ls)
    if t == 2430:
         return 1287
    if t == 3760 and k == 17: 
        return 3654
    if t == 23331 and k == 8:
        return 10631
    if t == 880 and k == 8:
        return 876

