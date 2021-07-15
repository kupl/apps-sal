def bingo(array): 
    return 'LOSE' if set('bingo') - set(chr(i + 96) for i in array) else 'WIN'
