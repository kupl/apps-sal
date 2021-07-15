import re

new_list = []
for _ in range(int(input())):
    s = re.sub(r'[^\w\s]','',input())
    new_list.append(s.split()[::-1])
    
for val in new_list[::-1]:
    print(' '.join(val))
