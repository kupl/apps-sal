from statistics import mean, median

def convert_ToInt(s):
    v = s.split('|')
    return sum(int(v[i]) * 60**(2-i) for i in range(3))

def convert_ToStr(n):
    return "{:0>2}|{:0>2}|{:0>2}".format(*map(int, (n//3600, n%3600 // 60, n%60)))

def stat(strg):
    if not strg: return ""
    
    data = list(map(convert_ToInt, strg.split(', ')))
    return "Range: {} Average: {} Median: {}".format(*map(convert_ToStr, [max(data)-min(data), mean(data), median(data)]))
