def d1d2(p,q,r,a,b,c):
    if p == 0 or q == 0 or r == 0:
        return False
    if a%p == 0 and b % q == 0:
        d1 = a//p
        d2 = b//q
        if c == r * d1 * d2:
            return True
        return False
    return False
    
def e1e2(p,q,r,a,b,c):
    e1 = a - p
    e2 = b - q
    return c == r + e1 + e2
        
def d3e3(p,q,r,a,b,c):
    delta = [0, 0, 0]
    delta[0] = p - q
#     print(f'1.{delta=}')
    if delta[0] == 0:
        return False
        # explanation:
        # for infinite no of sols a = b; but q = p(delta[0] == 0) sol 2 same case (already handled) not considering here
    delta[1] = a - b
    delta[2] = p*b - q*a
#     print(f'2.{delta=}')
    if delta[1] % delta[0] == 0 and delta[2] % delta[0] == 0:
        val_d = delta[1]//delta[0]
        val_e = delta[2]//delta[0]
        return  c == r * val_d + val_e
            
    else:
        #e and d are not integer solutions
        return False
         
def d3e2(p,q,r,a,b,c):
    #assuming a,b eq has same form
    delta = [0, 0, 0]
    delta[0] = p - q
    if delta[0] == 0:
        return False
        # explanation:
        # for infinite no of sols a = b; but q = p(delta[0] == 0) sol 2 same case (already handled) not considering here
    delta[1] = a - b
    delta[2] = p*b - q*a
#     print(f'Δ0 = {delta[0]} Δ1 = {delta[1]} Δ2 = {delta[2]}')
    if delta[1] % delta[0] == 0 and delta[2] % delta[0] == 0:
        val_d = delta[1]//delta[0]
        val_e = delta[2]//delta[0]
#         print(f'd = {val_d} e = {val_e}')
        return  c == r * val_d
            
    else:
        #e and d are not integer solutions
        return False
        
def d2e3(p,q,r,a,b,c):
    #assuming a,b eq has same form
    
    delta = [0, 0, 0]
    delta[0] = p - q
    if delta[0] == 0:
        return False
        # explanation:
        # for infinite no of sols a = b; but q = p(delta[0] == 0) sol 2 same case (already handled) not considering here
    delta[1] = a - b
    delta[2] = p*b - q*a

    if delta[1] % delta[0] == 0 and delta[2] % delta[0] == 0:
        val_d = delta[1]//delta[0]
        val_e = delta[2]//delta[0]
        return  c == r + val_e
            
    else:
        #e and d are not integer solutions
        return False
        
'''
two case: 1. a = pd + e, b = qd + e, c = r (already handled 1 same)
2. a = pd + e, b = qd, c = r + e
'''
def d2e2(p,q,r,a,b,c):
    if q != 0 and b % q == 0:
        d = b//q
        e = c - r
        assert e != 0, "already checked, one same"
        return a == p*d + e
    return False

def e3d2(p,q,r,a,b,c):
    assert c!=r, "1 same"
    e = c - r
    if p != -e and q !=-e and a % (p + e) == 0 and b % (q + e) == 0:# p + e != 0 as then a = 0 and 1 difference case or no soln
        d1 = a//(p + e)
        d2 = b//(q + e)
        return d1 != 1 and d1 == d2
    return False
    
def e2d2(p,q,r,a,b,c):
    if r != 0 and c % r == 0:
        d = c//r
        e = b - q
        assert d != 1 and e != 0, '1 or 2 same'
        return a == (p + e) * d
    return False
    
def modified(src, dst):
    p,q,r = src
    a,b,c = dst
    # print(p,q,r), '-->',(a,b,c)
    
    #case 1: some are same
    #case 1.0: all are same then 0 chances:
    if p == a and q == b and r == c:
        print(0)
        return
    #case 1.1:if two are same
    # p,q
    if p == a and q == b:
        if r != c:
            print(1)
            return
        assert True, "Should not have come here1"
    # q,r
    if q == b and r == c:
        if p != a:
            print(1)
            return
        assert True, "Should not have come here2"
    # r,p
    if r == c and p == a:
        if q != b:
            print(1)
            return
        assert True, "Should not have come here3"
        
    #case 1.3 any one is same
    # p
    if p == a:
        if b - q == c - r:
            print(1)
            return
        if q != 0 and r != 0 and b%q == 0 and b%q == c%r and b//q == c//r:
            print(1)
            return
        print(2)
        return
    if q == b:
        if c - r == a - p:
            print(1)
            return
        if p != 0 and r != 0 and a%p == 0 and  a%p == c%r and a//p == c//r:
            print(1)
            return
        print(2)
        return
        
    if r == c:
        if b - q == a - p:
            print(1)
            return
        if p != 0 and q != 0 and a%p == 0 and  a%p == b%q and a//p == b//q:
            print(1)
            return
        print(2)
        return        
    #case 2: all are different
    #case 2.1: all are at same difference : 2 same ratio/ difference
    if p-a == q-b and q-b == r-c:
        print(1)
        return
    #or at same ratio
    if p!=0 and q!= 0 and r!=0:
        if a%p == 0 and a%p == b%q and b%q == c%r:
            if a//p == b//q and b//q == c//r:
                print(1)
                return
    #if any two has same difference or ratio
    #case 2.2: 1 same ratio/difference
    # p,q
    if p-a == q-b :
        print(2)
        return
    if p!=0 and q!=0 and a%p == 0 and a%p == b%q and a//p == b//q:
        print(2)
        return
    # q,r
    if r-c == q-b :
        print(2)
        return
    if r!=0 and q!=0 and c%r == 0 and c%r == b%q and c//r == b//q:
        print(2)
        return    
    
    # r,p
    if p-a == r-c :
        print(2)
        return
    if p!=0 and r!=0 and a%p == 0 and a%p == c%r and a//p == c//r:
        print(2)
        return
    
    
    #case 3: nothing is same no two has same difference or ration
    #case 3.0: pd1 qd2 rd1d2 form
    if d1d2(p,q,r,a,b,c) or d1d2(q,r,p,b,c,a) or d1d2(r,p,q,c,a,b):
        print(2)
        return
    #case 3.1: p + e1 q + e2 r + e1 + e2 form
    if e1e2(p,q,r,a,b,c) or e1e2(q,r,p,b,c,a) or e1e2(r,p,q,c,a,b):
        print(2)
        return
    #case 3.2: pd + e forms
    #case 3.2.1: 3d3e
    if d3e3(p,q,r,a,b,c):
        print(2)
        return
    #case 3.2.2: 3d2e
    if d3e2(p,q,r,a,b,c) or d3e2(q,r,p,b,c,a) or d3e2(r,p,q,c,a,b):
        print(2)
        return
    
    #case 3.2.3: 2d3e
    if d2e3(p,q,r,a,b,c) or d2e3(q,r,p,b,c,a) or d2e3(r,p,q,c,a,b):
        print(2)
        return
    if d2e2(p,q,r,a,b,c) or d2e2(q,r,p,b,c,a) or d2e2(r,p,q,c,a,b) or d2e2(p,r,q,a,c,b) or d2e2(q,p,r,b,a,c) or d2e2(r,q,p,c,b,a):
        print(2)
        return
    if e3d2(p,q,r,a,b,c) or e3d2(q,r,p,b,c,a) or e3d2(r,p,q,c,a,b):
        print(2)
        return
    if e2d2(p,q,r,a,b,c) or e2d2(q,r,p,b,c,a) or e2d2(r,p,q,c,a,b) or e2d2(p,r,q,a,c,b) or e2d2(q,p,r,b,a,c) or e2d2(r,q,p,c,b,a):
        print(2)
        return
    print(3)
    
for _ in range(int(input())):
    src = tuple(map(int, input().split()))
    dst = tuple(map(int, input().split()))
    modified(src, dst)
    # print(modified(src, dst))
