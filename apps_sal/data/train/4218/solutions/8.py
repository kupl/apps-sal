def game_winners(*args):
    (a,b),(c,d) = args
    sg, ss = a + 150 * (b=='yes'), c + 150 * (d=='yes')
    return ["It's a draw!","Gryffindor wins!","Slytherin wins!"][(sg>ss)-(sg<ss)]
