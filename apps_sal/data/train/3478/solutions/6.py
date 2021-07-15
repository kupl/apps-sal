def battle(player1, player2):
  rem1=[c for i,c in enumerate(player1) if i>=len(player2) or c[1]>player2[i][0]]
  rem2=[c for i,c in enumerate(player2) if i>=len(player1) or c[1]>player1[i][0]]
  return {'player1':rem1, 'player2':rem2}
