from datetime import datetime

def to12hourtime(t):
    return datetime.strptime(t, '%H%M').strftime('%I:%M %p').lstrip('0').lower()
