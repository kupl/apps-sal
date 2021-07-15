from functools import reduce
from itertools import combinations_with_replacement 

''' Naive implementation of combinations built incrementaly doesn't work (for k = 3, there's no 1,2,3): 
n = 5
for k in range(1,n):
    k_uplet_init = [1 for item in range(k)]
    print(k_uplet_init)
    for i in range(1,2*n):
        k_uplet_init[k_uplet_init.index(min(k_uplet_init))] += 1
        print(k_uplet_init)
'''
    
    
'''    
def productsum(n):
    result = []
    collections = [(2,2)]
    
    #setting up the various digits needed
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    
    print('nums are {0}'.format(nums))
    #initiate k
    for k in range(2,n+1):
        print('k = {0}'.format(k))
        #loops through digits to use in nums
        for digits in nums:
            print('digits = {0}'.format(digits))
            
            combi = [uplets for uplets in list(combinations_with_replacement(digits, k))]
            print('k combination of digits is {0}'.format(combi))
            for item in combi:
                print('n_uplet is {0}'.format(item))
                sums = sum(item)
                print('sum = {0}'.format(sums))
                prods = reduce(lambda x,y: x*y,item)
                print('prod = {0}\n'.format(prods))
                if sums == prods:
                    if item not in collections:
                        if len(item) == len(collections[-1]):
                            if sum(item) < sum(collections[-1]):
                                print('appending item {0}'.format(item))
                                collections[-1] = item
                                print('collection is now {0}\n'.format(collections))
                        else:
                            print('appending item {0}'.format(item))
                            collections.append(item)
                            print('collection is now {0}\n'.format(collections))
                    break
          
    #collections = collections[1:]
    
    for item in collections:
        if sum(item) not in collections:
            result.append(sum(item))
    
    result = list(set(result))
    
    return sum(result)
'''
'''
def productsum(n):
    result = []
    collections = [(2,2)]
    
    #setting up the various digits needed
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    
    #initiate k
    for k in range(2,n+1):
        #loops through digits to use in nums
        for digits in nums:
            combi = [uplets for uplets in list(combinations_with_replacement(digits, k))]
            for item in combi:
                sums = sum(item)
                prods = reduce(lambda x,y: x*y,item)
                if sums == prods:
                    if item not in collections:
                        if len(item) == len(collections[-1]):
                            if sum(item) < sum(collections[-1]):
                                collections[-1] = item
                        else:
                            collections.append(item)
                    break
          
    for item in collections:
        if sum(item) not in collections:
            result.append(sum(item))
    
    print('collection is  {0}\n'.format(collections))
    print('result is  {0}\n'.format(result))
    result = list(set(result))
    print('final result (sum) is  {0}\n'.format(sum(result)))
    return sum(result)
    '''

'''
def productsum(n):
    result = []
    collections = [(2,2)]
    sums = []
    
    #setting up the various digits needed
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    
    #initiate k
    for k in range(2,n+1):
        #loops through digits to use in nums
        #print('k = {0}'.format(k))
        for digits in range(k):
            #print('digits = {0}'.format(nums[digits]))
            combi = [uplets for uplets in list(combinations_with_replacement(nums[digits], k)) if sum(uplets) == reduce(lambda x,y: x*y,uplets)]
            #print('combinations valid are: {0}'.format(combi))
            if len(combi) > 0:
                combi_sum = [sum(items) for items in combi]
                collections.append(combi[combi_sum.index(min(combi_sum))])
                break
    for item in collections:
        if sum(item) not in collections:
            result.append(sum(item))
    #print('collection is  {0}\n'.format(collections))
    #print('result is  {0}\n'.format(result))
    result = list(set(result))
    #print('final result (sum) is  {0}\n'.format(sum(result)))
    return sum(result)
'''

'''
def productsum(n):

    n_uplets = [()]
    result = []
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    print(nums)
    counter = 1
    while len(n_uplets) < n+1:
        for digits in nums:
            combi = [uplets for uplets in list(combinations_with_replacement(digits, counter))]
            #print('combi is {0}'.format(combi))
            for combis in combi:
                #sums = sum(combis)
                prods = reduce(lambda x,y: x*y,combis)
                if sum(combis) == prods:
                    if len(n_uplets[-1]) == len(combis):
                        if sum(combis) < sum(n_uplets[-1]):
                            n_uplets[-1] = combis
                    else:
                        n_uplets.append(combis)

            #print('n_uplets = {0}'.format(n_uplets))
            counter +=1
    n_uplets = n_uplets[2:]
    print('final n_uplets are {0}'.format(n_uplets))

    result = [sum(el) for el in n_uplets]
    result = list(set(result))

    return sum(result)
'''

from functools import reduce
from itertools import combinations_with_replacement 

''' Naive implementation of combinations built incrementaly doesn't work (for k = 3, there's no 1,2,3): 
n = 5
for k in range(1,n):
    k_uplet_init = [1 for item in range(k)]
    print(k_uplet_init)
    for i in range(1,2*n):
        k_uplet_init[k_uplet_init.index(min(k_uplet_init))] += 1
        print(k_uplet_init)
'''
    
    
'''    
def productsum(n):
    result = []
    collections = [(2,2)]
    
    #setting up the various digits needed
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    
    print('nums are {0}'.format(nums))
    #initiate k
    for k in range(2,n+1):
        print('k = {0}'.format(k))
        #loops through digits to use in nums
        for digits in nums:
            print('digits = {0}'.format(digits))
            
            combi = [uplets for uplets in list(combinations_with_replacement(digits, k))]
            print('k combination of digits is {0}'.format(combi))
            for item in combi:
                print('n_uplet is {0}'.format(item))
                sums = sum(item)
                print('sum = {0}'.format(sums))
                prods = reduce(lambda x,y: x*y,item)
                print('prod = {0}\n'.format(prods))
                if sums == prods:
                    if item not in collections:
                        if len(item) == len(collections[-1]):
                            if sum(item) < sum(collections[-1]):
                                print('appending item {0}'.format(item))
                                collections[-1] = item
                                print('collection is now {0}\n'.format(collections))
                        else:
                            print('appending item {0}'.format(item))
                            collections.append(item)
                            print('collection is now {0}\n'.format(collections))
                    break
          
    #collections = collections[1:]
    
    for item in collections:
        if sum(item) not in collections:
            result.append(sum(item))
    
    result = list(set(result))
    
    return sum(result)
'''
'''
def productsum(n):
    result = []
    collections = [(2,2)]
    
    #setting up the various digits needed
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    
    #initiate k
    for k in range(2,n+1):
        #loops through digits to use in nums
        for digits in nums:
            combi = [uplets for uplets in list(combinations_with_replacement(digits, k))]
            for item in combi:
                sums = sum(item)
                prods = reduce(lambda x,y: x*y,item)
                if sums == prods:
                    if item not in collections:
                        if len(item) == len(collections[-1]):
                            if sum(item) < sum(collections[-1]):
                                collections[-1] = item
                        else:
                            collections.append(item)
                    break
          
    for item in collections:
        if sum(item) not in collections:
            result.append(sum(item))
    
    print('collection is  {0}\n'.format(collections))
    print('result is  {0}\n'.format(result))
    result = list(set(result))
    print('final result (sum) is  {0}\n'.format(sum(result)))
    return sum(result)
    '''

'''
def productsum(n):
    result = []
    collections = [(2,2)]
    sums = []
    
    #setting up the various digits needed
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    
    #initiate k
    for k in range(2,n+1):
        #loops through digits to use in nums
        #print('k = {0}'.format(k))
        for digits in range(k):
            #print('digits = {0}'.format(nums[digits]))
            combi = [uplets for uplets in list(combinations_with_replacement(nums[digits], k)) if sum(uplets) == reduce(lambda x,y: x*y,uplets)]
            #print('combinations valid are: {0}'.format(combi))
            if len(combi) > 0:
                combi_sum = [sum(items) for items in combi]
                collections.append(combi[combi_sum.index(min(combi_sum))])
                break
    for item in collections:
        if sum(item) not in collections:
            result.append(sum(item))
    #print('collection is  {0}\n'.format(collections))
    #print('result is  {0}\n'.format(result))
    result = list(set(result))
    #print('final result (sum) is  {0}\n'.format(sum(result)))
    return sum(result)
'''

'''
def productsum(n):

    n_uplets = [()]
    result = []
    nums = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    print(nums)
    counter = 1
    while len(n_uplets) < n+1:
        for digits in nums:
            combi = [uplets for uplets in list(combinations_with_replacement(digits, counter))]
            #print('combi is {0}'.format(combi))
            for combis in combi:
                #sums = sum(combis)
                prods = reduce(lambda x,y: x*y,combis)
                if sum(combis) == prods:
                    if len(n_uplets[-1]) == len(combis):
                        if sum(combis) < sum(n_uplets[-1]):
                            n_uplets[-1] = combis
                    else:
                        n_uplets.append(combis)

            #print('n_uplets = {0}'.format(n_uplets))
            counter +=1
    n_uplets = n_uplets[2:]
    print('final n_uplets are {0}'.format(n_uplets))

    result = [sum(el) for el in n_uplets]
    result = list(set(result))

    return sum(result)
'''

'''
def productsum(n):
    print('n = {0}'.format(n))
    n_uplets = []
    result = []
    nums = []
    not_min = []
    for i in range(3,n+3):
        nums.append([item for item in range(1,i)])
    nums = nums[-2:]
    #print('nums = {0}'.format(nums))
    counter = 2
    for digits in nums:
        if len(n_uplets) <= n:          
            #print('\ndigits = {0}'.format(digits))
            combi = [uplets for uplets in list(combinations_with_replacement(digits, counter))]
            #print('combi is {0}\n'.format(combi))
            for combis in combi:
                prods = reduce(lambda x,y: x*y,combis)
                x = prods - sum(combis)
                solution = tuple(1 for item in range(1,x+1))

                z = combis + solution
                z = sorted(z)
                z = tuple(z)
                if sum(z) == prods and len(z) <= n:
                    #print('z is {0}'.format(z))
                    if tuple(z) not in n_uplets :
                        y = [len(member) for member in n_uplets]
                        if len(z) in y and sum(z) < sum(n_uplets[y.index(len(z))]):
                            not_min.append(n_uplets[y.index(len(z))])
                            if z not in not_min:
                                n_uplets[y.index(len(z))] = z
                                #print('replacing uplets with z = {0}'.format(z))
                            #print('z IGNORED {0}'.format(z))
                        else:
                            if z not in not_min and len(z) not in y:
                                n_uplets.append(z)
                                #print('adding uplets z = {0}'.format(z))
                            
                        #print('n_uplets is now {0}'.format(n_uplets))
            counter +=1
            
    print('final n_uplets are {0}'.format(n_uplets))
    print('not_minimums are {0}'.format(not_min))
    result = [sum(el) for el in n_uplets]
    result = list(set(result))
    print('result before sum is {0}'.format(result))
    return sum(result)

'''
def productsum(n):
    if n < 12:
        kmax = n+1
    else:
        kmax = n
    
    def prodsum(p, s, nf, start):
        k = p - s + nf     # product - sum + number of factors
        if k < kmax:
            if p < n[k]:
                n[k] = p
            for i in range(start, kmax//p*2 + 1):
                prodsum(p*i, s+i, nf+1, i)
    if kmax > 12: kmax +=1
    n = [2*kmax] * kmax
    
    prodsum(1, 1, 1, 2)
    
    return sum(set(n[2:]))


