def get_percentage(sent, limit=1000):
    return "No e-mails sent" if sent == 0 else "Daily limit is reached" if sent >= limit else "{}%".format((100*sent)//limit)
