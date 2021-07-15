from functools import reduce
import itertools

def most_common(lst):
    return max(set(lst), key=lst.count)


def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def gcd_list(alist):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a


    result = alist[0]
    for i in alist[1:]:
        result = gcd(result, i)

    return result



def common_subs(alist):
    to_return = []
    for i in alist:
        for j in alist:
            if i != j:
                to_return.append(abs(i-j))
    return to_return
    
#print(common_subs([100,3,4]))    


def get_key_length(cipher_text,max_key_length):
    dis = []
    for pos,char in enumerate(cipher_text):
        if pos == len(cipher_text)-1:
            pass
        else:
            dis.append([cipher_text[pos]+cipher_text[pos+1],pos])
            
    alls = []
    for di in dis:
        if [x[0] for x in dis].count(di[0]) != 1:
            a = [x[1] for x in dis if x[0] == di[0]]
            #print(a)
            #print(common_subs(a))
            #print(gcd_list(common_subs(a)))
            alls.append(gcd_list(common_subs(a)))
    print('a')
    return most_common([x for x in alls if x != 1])
            
            

