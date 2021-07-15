def is_lucky(ticket):
    try:
        return sum(int(ticket) // 10**i % 10 * complex(0, 1)**(i // 3 * 2) for i in range(6)) == 0
    except:
        return False
