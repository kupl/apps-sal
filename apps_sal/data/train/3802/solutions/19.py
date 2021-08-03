def hoop_count(n):
    msg = ["Keep at it until you get it", "Great, now move on to tricks"]
    if n >= 10:
        return msg[1]
    elif n < 10:
        return msg[0]
