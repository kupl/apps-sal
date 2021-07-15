##row, col, order = input().split(' ')    
##row = int(row)
##col = int(col)
##
##init_list = []
##
##for i in range(row):
##    init_list.append(input().split(' '))
##
##if order=='0':
##    for i in range(row):
##        print()
##        for j in range(col,0,-1):
##            print(init_list[i][j-1], end = ' ')
##else:
##    for i in range(row,0,-1):
##        print()
##        for j in range(col):
##            print(init_list[i-1][j], end = ' ')

def judge(_list:list) -> int:
    number = -1
    for i in range(len(_list)):
        if int(_list[i]) == i+1:
            number += 1
        else:
            pass
    
    return number

mat_num, chain_num = input().split(' ')
mat_num, chain_num = int(mat_num), int(chain_num)

chain = []

for i in range(chain_num):
    chain.append([])
    temp_list = input().split(' ')
    for j in range(int(temp_list[0])):
        chain[-1].append(temp_list[1])
        del temp_list[1]

for i in range(chain_num):
    if judge(chain[i]) < 1:
        pass
    else:
        temp_count = len(chain[i]) - judge(chain[i])
        chain[i] = []
        for j in range(temp_count):
            chain[i].append(1)

time = 0
count = 0

for i in range(chain_num):
    time += len(chain[i]) - 1
    count += len(chain[i])

print(time + count -1)

