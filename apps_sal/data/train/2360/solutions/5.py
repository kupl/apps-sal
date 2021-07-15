N = int(input())
b = bin(N)[2:][::-1]
count = len(b)-1

def print_matrix(m):
    print(len(m))
    for i in range(len(m)):
        print("".join(m[i]))

m = [['N' for i in range(2*(len(b))+count)] for j in range(2*(len(b))+count)]
for i in range(count-1):
    val = len(m)-count+i
    m[val][val+1] = 'Y'
    m[val+1][val] = 'Y'

if count>0:
    m[len(m)-1][1] = 'Y'
    m[1][len(m)-1] = 'Y'

#print_matrix(m)
c = 0
c2 = len(m)-count
for i in range(0, len(m)-count, 2):
    if i >= len(m)-2-count and i != 0:
        m[i][1] = 'Y'
        m[i+1][1] = 'Y'
        m[1][i+1] = 'Y'
        m[1][i] = 'Y'
    elif i < len(m)-2-count:
        m[i][i+2] = 'Y'
        m[i][i+3] = 'Y'
        m[i+2][i] = 'Y'
        m[i+3][i] = 'Y'
        if i != 0:
       	    m[i+1][i+2] = 'Y'
       	    m[i+1][i+3] = 'Y'
       	    m[i+2][i+1] = 'Y'
       	    m[i+3][i+1] = 'Y'
    if b[c] =='1':
        if i == len(m)-count-2:
            c2 = 1
        #print_matrix(m)
        m[i][c2] = 'Y'
        m[c2][i] = 'Y'
        if i != 0:
            m[i+1][c2] = 'Y'
            m[c2][i+1] = 'Y'
    c2+=1
        #print_matrix(m)
    c+=1

print(len(m))
for i in range(len(m)):
    print("".join(m[i]))


