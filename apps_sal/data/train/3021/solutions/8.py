def available_moves(pos):
    if type(pos)!=str or pos[0] not in 'ABCDEFGH' or pos[1:] not in '12345678':return []
    i, j = int(pos[1]) - 1, 'ABCDEFGH'.index(pos[0])
    final = sorted(set([f"{i}{pos[1]}"for i in 'ABCDEFGH']+[f"{pos[0]}{i}"for i in range(1, 9)]+find(i,j)+find(i,j,1,-1)))
    final.remove(pos)
    return final
def find(x, y, o=1, p=1,A = lambda a, b: f"{'ABCDEFGH'[a]}{b + 1}"):
        while 0 <= x <= 7 and 0 <= y <= 7 : x -= o ; y -= p
        x += o ; y += p ; li = []
        while 0 <= x < 8 and 0 <= y < 8:
            li.append(A(y, x)) ; x += o ; y += p
        return li
