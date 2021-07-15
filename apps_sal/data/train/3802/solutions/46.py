def hoop_count(n):
    msg1 = 'Great, now move on to tricks'
    msg2 = 'Keep at it until you get it'
    return (msg1, msg2)[n < 10]
