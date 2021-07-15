def hoop_count(n):
    return {
    True: "Great, now move on to tricks",
    False: "Keep at it until you get it"
    }.get(n >= 10)
