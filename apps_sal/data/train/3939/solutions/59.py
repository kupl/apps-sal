def rps(a:str,b:str):
  c:str = "Player 1 won!"
  d:str = "Player 2 won!"
  e:str = "Draw!"  
  if a == "rock" and b == "scissors":
    return c
  if a == "scissors" and b == "paper":
    return c
  if a == "paper" and b == "rock":
    return c
  if a == "rock" and b == "paper":
    return d
  if a == "scissors" and b == "rock":
    return d
  if a == "paper" and b == "scissors":
    return d
  else:
    return e    
