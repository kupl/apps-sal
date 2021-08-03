
def row(array, j):
    for i in range(len(array[0])):
        if(array[j][i] == 0):
            array[j][i] = 1
        else:
            array[j][i] = 0


def col(array, j):
    for i in range(len(array)):
        if(array[i][j] == 0):
            array[i][j] = 1
        else:
            array[i][j] = 0


m, n = list(map(int, input().split(" ")))
lt = []
for i in range(m):
    temp = list(map(int, input().split(" ")))
    lt.append(temp)
for i in range(len(lt)):
    if(lt[i][0] == 0):
        row(lt, i)

for i in range(1, len(lt[0])):
    count1 = 0
    count0 = 0
    for j in range(len(lt)):
        if(lt[j][i] == 0):
            count0 = count0 + 1
        else:
            count1 = count1 + 1
    if(count0 > count1):
        col(lt, i)
st = []
for i in range(len(lt)):
    temp1 = ""
    for j in range(len(lt[i])):
        temp1 = temp1 + str(lt[i][j])
    st.append(temp1)
ans = 0
# print(st)
for i in range(len(st)):
    ans = ans + int(st[i], 2)
print(ans)
