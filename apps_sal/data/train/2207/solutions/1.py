n=int(input())
live1, dead1, live2, dead2 = 0, 0, 0, 0
for i in range(n):
    I=[int(j) for j in input().split()]
    if I[0]==1:
        live1+=I[1]
        dead1+=I[2]
    else:
        live2+=I[1]
        dead2+=I[2]
if live1>=(live1+dead1)/2: print('LIVE')
else: print('DEAD')
if live2>=(live2+dead2)/2: print('LIVE')
else: print('DEAD')
