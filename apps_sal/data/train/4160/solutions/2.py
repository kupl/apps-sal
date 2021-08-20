def get_percentage(sent, limit=1000):
    return f'{100 * sent // limit}%' if 0 < sent < limit else 'Daily limit is reached' if sent else 'No e-mails sent'
