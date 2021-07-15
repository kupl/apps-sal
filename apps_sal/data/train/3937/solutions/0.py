def check(num,max_sum):
    l = [int(i) for i in str(num)]
    for i in range(0,len(l) - 3):
        if sum(l[i:i+4]) > max_sum:return False
    return True

def max_sumDig(nMax, maxSum):
    found = [i for i in range(1000,nMax + 1) if check(i,maxSum)]
    mean = sum(found) / float(len(found))
    for i in range(len(found) - 1):
        if abs(mean - found[i]) < abs(mean - found[i + 1]):
            mean = found[i]
            break
    return [len(found), mean, sum(found)]
