def get_percentage(sent, limit=1000):
    return "No e-mails sent" if not sent \
        else "%d%%" % (100*sent//limit) if sent < limit \
            else "Daily limit is reached"
