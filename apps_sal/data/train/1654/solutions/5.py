import re

def solve_runes(runes):
    # 分解
    m = re.match(r'(-?[0-9?]+)([-+*])(-?[0-9?]+)=(-?[0-9?]+)', runes)
    nums = [m.group(1),m.group(3),m.group(4)]
    op = m.group(2)
    
    # 迭代尝试
    for v in range(0,10):
        # 同字校验
        if str(v) in runes:
            continue
            
        testNums = [num.replace('?',str(v)) for num in nums]
        
        # 0起始校验
        for num in testNums:
            if re.match(r"(^0|^(-0))[0-9]+",num):
                break
        else:
            # 判等
            if int(testNums[2]) == eval(testNums[0] + op + testNums[1]):
                return v
    
    return -1 
