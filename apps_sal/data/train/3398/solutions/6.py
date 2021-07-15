import numpy as np
def solve(arr):
    l = len(arr)
    fst = arr[0]
    lst = arr[l-1]
    diff_range = lst - fst
    diffs = []
    for diff in range(diff_range - 2, diff_range + 3):
        if diff == 0:
            diffs.append(diff)
        elif diff % (l - 1) == 0:
            diffs.append(diff)
    
    progs = []
    for diff in diffs:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if fst + i + diff == lst + j:
                  seq = []
                  if diff == 0:
                    seq = l * [fst+i]
                  else:
                    k = 1
                    if diff < 0:
                        k = -1 
                    seq = list(np.arange(fst + i, lst + j + k, diff / (l - 1)))
                  if len(seq) == l:
                      progs.append(seq)
      
    changes = []
    for seq in progs:
        change = 0
        complete = True
        for a,b in zip(seq,arr):
            diff = abs(a-b)
            if diff > 1:
              complete = False
              continue
            if diff != 0:
              change += 1
        if complete:
          changes.append(change)
  
    if len(changes) == 0:
      return -1
    return min(changes)

