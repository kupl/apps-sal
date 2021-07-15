def crashing_weights(weights):
    w=zip(*weights)
    ans=[]
    for i in w:
        i=list(i)[::-1]
        while len(i)>1 and i!=sorted(i, reverse=True):
            for j in range(len(i)-1,0,-1):
                if i[j-1]<i[j]:
                    i[j-1]+=i[j]
                    del i[j]
                    break
        ans.append(i[0])
    return ans
