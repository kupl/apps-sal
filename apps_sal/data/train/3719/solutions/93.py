from decimal import Decimal


def starting_mark(height):

    #     if height == 1.22:
    #         return 8.27
    #     elif height == 2.13:
    #         return 11.85

    number = Decimal("0.03935483870967741935483870968")
    start = Decimal("8.27")
    height = Decimal(height)
    min_height = Decimal("1.22")

    form = (height - min_height) * 100 * number + start
    form = form.quantize(Decimal("1.00"))
    form = float(form)
    return form
