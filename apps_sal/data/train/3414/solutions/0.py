import re
def reversi_row(moves):
    row = '........'
    stones = '*O'
    for i, m in enumerate(moves):
        L, M, R = row[:m], stones[i%2], row[m+1:]
        if R!='' and R[0] == stones[(i+1)%2] and R.find(stones[i%2])>0 and '.' not in R[:R.find(stones[i%2])]:
            R = R.replace(stones[(i+1)%2], stones[i%2], R.find(stones[i%2]))
        if L!='' and  L[-1] == stones[(i+1)%2] and L[::-1].find(stones[i%2])>0 and '.' not in L[-1-L[::-1].find(stones[i%2]):]:
            L = L[::-1].replace(stones[(i+1)%2], stones[i%2], L[::-1].find(stones[i%2]))[::-1]

        row = L + M + R
    return row
