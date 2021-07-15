deltas = dict(zip("←↑→↓↖↗↘↙", (-1,-1j,1,1j,-1-1j,1-1j,1+1j,-1+1j)))

def count_deaf_rats(town_square):
    ii,jj = list(range(len(town_square[0]))),list(range(len(town_square)))
    p = next(complex(i,j) for i in ii for j in jj if town_square[j][i] == "P")
    return sum( abs(ij+d-p) > abs(ij-p) for ij,d in
        ((complex(i,j),deltas.get(town_square[j][i],0)) for j in jj for i in ii) )
