def is_lucky(ticket):
    try:
        if ticket == '':
            return False
        else:
            idk = [int(x) for x in ticket]
            first = sum(idk[0:3])
            second = sum(idk[3:6])
            if first == second:
                return True
            else:
                return False
    except:
        return False
