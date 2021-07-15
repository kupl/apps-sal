from typing import*
def areYouPlayingBanjo(name:List[str])->str:
  Yes:str = name + " plays banjo" 
  No:str = name + " does not play banjo"
  if name[0] == "r" or name[0] == "R":
    return Yes
  else:
    return No    

