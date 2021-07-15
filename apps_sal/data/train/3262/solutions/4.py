def is_palindrome(a,b):
    if len(a)!=len(b):
        return False
    else:
        for i in range(1,len(a)):
            if a.lower()[i:] + a.lower()[:i] == b.lower():
                return True
        return False
def group_cities(seq): 
    ans=[]
    already_chosen=[]
    for term in seq:
        if term not in already_chosen:
            temp=[term]
            already_chosen.append(term)
            for thing in seq:
                if thing not in already_chosen and thing!=term and is_palindrome(thing,term):
                    temp.append(thing)
                    already_chosen.append(thing)
            ans.append(temp)
    for thing in ans:
        thing.sort()
    ans.sort(key=lambda x:x[0])
    ans.sort(key=len,reverse=True)
    return ans
                    

