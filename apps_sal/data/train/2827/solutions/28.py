def switch_it_up(n):

    def zero():
        return 'Zero'

    def one():
        return 'One'

    def two():
        return 'Two'

    def three():
        return 'Three'

    def four():
        return 'Four'

    def five():
        return 'Five'

    def six():
        return 'Six'

    def seven():
        return 'Seven'

    def eight():
        return 'Eight'

    def nine():
        return 'Nine'
    options = {None: zero, 0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}
    return options[n]()
