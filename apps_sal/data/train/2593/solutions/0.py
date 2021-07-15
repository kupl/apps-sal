def minion_game(string):
    n=len(string)
    player1,player2=0,0
    for i in range(0,n):
        if(string[i] in 'AEIOU'):
            player1+=n-i
        else:
            player2+=n-i
    if(player1>player2):
        return 'Kevin '+ str(player1)
    elif(player1==player2):
        return 'Draw'
    else:
        return 'Stuart '+str(player2)
