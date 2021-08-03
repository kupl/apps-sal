def bingo(ticket, win):
    return 'Winner!' if sum(chr(arr[1]) in arr[0] for arr in ticket) >= win else 'Loser!'
