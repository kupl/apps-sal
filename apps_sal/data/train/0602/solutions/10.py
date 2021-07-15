# cook your dish here
s = input().strip()

s_arr = s.split()

res = "z" * 100000000
for ele in s_arr:
    if len(res) > len(ele):
        res = ele
    elif len(res) == len(ele):
        res = min(res, ele)
    
print(res, end = " ")
for ele in s_arr:
    print(ele, end = " ")
    print(res, end = " ")
