"""
from operator import itemgetter
inp=list(map(int, input().split()))
n, t = inp[0], inp[1]
array=inp[2:]
array.sort()
freq={}
for el in array:
    if el not in freq:
        freq[el]=1 
    else:
        freq[el]+=1
somme=[]
for i in range(n-1):
    for j in range(i+1,n):
        somme.append((array[i]+array[j], {i, j}))
somme.sort(key=itemgetter(0))
i_end=len(somme)-1
counter=0
computed={}
for i in range(len(somme)-1):
    while i_end>i and somme[i][0]+somme[i_end][0]>t:
        i_end-=1
    if i_end==i:
        break
    if somme[i][0]+somme[i_end][0]==t and len(somme[i][1]&somme[i_end][1])==0:
        id_start, i_mid1, i_mid2, id_end = sorted(somme[i][1]|somme[i_end][1])
        if (array[id_start], array[i_mid1], array[i_mid2], array[id_end]) not in computed:
            if array[id_start]==array[id_end]:
                appo=freq[array[id_start]]
                counter+=appo*(appo-1)*(appo-2)*(appo-3)//24
            elif array[id_start]==array[i_mid2]:
                appo=freq[array[i_mid1]]
                counter+=appo*(appo-1)*(appo-2)*freq[array[id_end]]//6
            elif array[id_end]==array[i_mid1]:
                appo=freq[array[i_mid1]]
                counter+=appo*(appo-1)*(appo-2)*freq[array[id_start]]//6
            elif array[id_start]==array[i_mid1] and array[id_end]==array[i_mid2]:
                counter+=freq[array[i_mid1]]*(freq[array[i_mid1]]-1)*freq[array[i_mid2]]*(freq[array[i_mid2]]-1)//4
            elif array[id_start]==array[i_mid1]:
                counter+=freq[array[i_mid1]]*(freq[array[i_mid1]]-1)*freq[array[i_mid2]]*freq[array[id_end]]//2
            elif array[id_end]==array[i_mid2]:
                counter+=freq[array[i_mid2]]*(freq[array[i_mid2]]-1)*freq[array[i_mid1]]*freq[array[id_start]]//2
            else:
                counter+=freq[array[id_start]]*freq[array[id_end]]*freq[array[i_mid1]]*freq[array[i_mid2]]
            computed[(array[id_start], array[i_mid1], array[i_mid2], array[id_end])]=1
print(counter)

array.sort()
freq={}
for el in array:
    if el not in freq:
        freq[el]=1 
    else:
        freq[el]+=1
counter=0
id_start=0
id_end=n-1
computed={}
for id_start in range(n-3):
    while id_end>id_start+2 and t-array[id_start]-array[id_end]<array[id_start+1]+array[id_start+2]:
        id_end-=1
    if id_end==id_start+2:
        break
    t_new=t-array[id_start]-array[id_end]
    i_mid2=id_end-1
    for i_mid1 in range(id_start+1, id_end-1):
        print(array[id_start], array[i_mid1], array[i_mid2], array[id_end])
        while i_mid2>i_mid1 and array[i_mid1]+array[i_mid2]>t_new:
            i_mid2-=1 
        if i_mid2==i_mid1:
            break
        if array[i_mid1]+array[i_mid2]==t_new and (array[id_start], array[i_mid1], array[i_mid2], array[id_end]) not in computed:
            if array[id_start]==array[id_end]:
                appo=freq[array[id_start]]
                counter+=appo*(appo-1)*(appo-2)*(appo-3)//24
            elif array[id_start]==array[i_mid2]:
                appo=freq[array[i_mid1]]
                counter+=appo*(appo-1)*(appo-2)*freq[array[id_end]]//6
            elif array[id_end]==array[i_mid1]:
                appo=freq[array[i_mid1]]
                counter+=appo*(appo-1)*(appo-2)*freq[array[id_start]]//6
            elif array[id_start]==array[i_mid1] and array[id_end]==array[i_mid2]:
                counter+=freq[array[i_mid1]]*(freq[array[i_mid1]]-1)*freq[array[i_mid2]]*(freq[array[i_mid2]]-1)//4
            elif array[id_start]==array[i_mid1]:
                counter+=freq[array[i_mid1]]*(freq[array[i_mid1]]-1)*freq[array[i_mid2]]*freq[array[id_end]]//2
            elif array[id_end]==array[i_mid2]:
                counter+=freq[array[i_mid2]]*(freq[array[i_mid2]]-1)*freq[array[i_mid1]]*freq[array[id_start]]//2
            else:
                counter+=freq[array[id_start]]*freq[array[id_end]]*freq[array[i_mid1]]*freq[array[i_mid2]]
            computed[(array[id_start], array[i_mid1], array[i_mid2], array[id_end])]=1
print(counter)
"""
nums = list(map(int, input().split()))
(n, t) = (nums.pop(0), nums.pop(0))
ways = [1] + [0] * t
nums.sort()
ans = 0
for i in range(2, n):
    if nums[i] > t - 3:
        break
    j = i - 1
    for k in range(0, j):
        if nums[k] + nums[j] > t - 2:
            break
        ways[nums[k] + nums[j]] += 1
    for last in range(i + 1, n):
        if nums[i] + nums[last] > t - 2:
            break
        left = t - nums[i] - nums[last]
        if left > 1:
            ans += ways[left]
print(ans)
