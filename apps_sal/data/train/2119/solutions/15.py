# Bosdiwale code chap kr kya milega
# Motherfuckers Don't copy code for the sake of doing it
# ..............
# ╭━┳━╭━╭━╮╮
# ┃┈┈┈┣▅╋▅┫┃
# ┃┈┃┈╰━╰━━━━━━╮
# ╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
# ╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉
# ╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤
# ╲┃┈┈┈┈╭━┳━━━━╯
# ╲┣━━━━━━┫
# ……….
# .……. /´¯/)………….(\¯`\
# …………/….//……….. …\\….\
# ………/….//……………....\\….\
# …./´¯/…./´¯\……/¯ `\…..\¯`\
# ././…/…/…./|_…|.\….\….\…\.\
# (.(….(….(…./.)..)...(.\.).).)
# .\…………….\/../…....\….\/…………/
# ..\…………….. /……...\………………../
# …..\…………… (………....)……………./

n = int(input())
arr = list(map(int,input().split()))
ind = list(map(int,input().split()))
parent = {}
rank = {}
ans = {}
total = 0
temp = []
def make_set(v):
    rank[v] = 1
    parent[v] = v
    ans[v] = arr[v]

def find_set(u):
    if u==parent[u]:
        return u
    else:
        parent[u] = find_set(parent[u])
    return parent[u]

def union_set(u,v):
    a = find_set(u)
    b = find_set(v)
    if a!=b:
        if rank[b]>rank[a]:
            a,b = b,a
        parent[b] = a
        rank[a]+=rank[b]
        ans[a]+=ans[b]
    return ans[a]

for i in range(n-1,-1,-1):
    rem = ind[i]-1
    make_set(rem)
    final = ans[rem]
    if rem+1 in parent:
        final = union_set(rem,rem+1)
    if rem-1 in parent:
        final = union_set(rem,rem-1)
    total = max(total,final)
    temp.append(total)
temp[-1] = 0
temp = temp[-1::-1]
temp = temp[1::]
for i in temp:
    print(i)
print(0)
