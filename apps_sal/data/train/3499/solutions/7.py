from datetime import datetime


def to24hourtime(hour, minute, period):
    return datetime.strptime(f"{hour} {minute} {period}", "%I %M %p").strftime("%H%M")
