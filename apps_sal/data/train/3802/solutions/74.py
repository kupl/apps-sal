def hoop_count(n):
    messages = ["Great, now move on to tricks", "Keep at it until you get it"]
    return messages[0] if n >= 10 else messages[1]
