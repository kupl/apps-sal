def get_diagonale_code(grid: str) -> str:
    ans=[]
    if grid:
      grid = [k.strip().split(" ") for k in grid.split("\n")]
      i=j=0
      dir = True
      while j <len(grid[i]):
        ans.append(grid[i][j])
        if i == len(grid) - 1:dir = False
        if (i == 0): dir = True 
        i = 0 if len(grid) == 1 else i +1 if dir else i - 1
        j+=1
    return "".join(ans)

