def over_the_road(address, n):
    if(address % 2):
        nth = ((address - 1) // 2) + 1
        event_nth = (n + 1) - nth
        print((2 + (event_nth - 1) * 2))
        return 2 + (event_nth - 1) * 2
    else:
        nth = ((address - 2) // 2) + 1
        odd_nth = (n + 1) - nth
        print((1 + (odd_nth - 1) * 2))
        return 1 + (odd_nth - 1) * 2
