def missing(s):
    for nd in range(1,min(7, len(s)//2+1)):
        guess, miss = s[:nd], ''
        n = int(guess)
        while len(guess) < len(s):
            n += 1
            guess += str(n)
            if not s.startswith(guess):
                if miss:
                    miss = ''
                    break
                miss = str(n)
                guess = guess[:-len(miss)]
        if miss: return int(miss)
    return -1
