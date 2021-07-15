def get_percentage(a, b=1000):
    return "No e-mails sent" if not a else "Daily limit is reached" if a >= b else f"{int(a / b * 100)}%"
