def missing(s):
    result = -1
    for start_chunk in range(1,len(s)//2 +1):
        res = inner(s,start_chunk)
        if res != -1:
            result = res
    return result

def inner(s,start_chunk):
    result = -1
    nums = []
    rest = s
    rip_count = 0
    last = int(rest[:start_chunk])
    rest = rest[start_chunk:]
    nums.append(last)
    chunk = start_chunk
    while rest!= '':
        if int(rest[:chunk]) - last != 1:
            if int(rest[:chunk+1]) - last == 1:
                chunk +=1
                print('chunk +=1')
            elif int(rest[:chunk+1]) - last == 2:
                chunk +=1
                rip_count+=1
                print('chunk +=1')
                print('rip_count+=1')
                result = last + 1
            elif int(rest[:chunk]) - last  == 2:
                rip_count+=1
                print('rip_count+=1')
                result = last + 1
            else: return -1
        nums.append(int(rest[:chunk]))
        last = int(rest[:chunk])
        rest = rest[chunk:]
        print(nums)
        if(rip_count)>1:
            return -1
    return result
