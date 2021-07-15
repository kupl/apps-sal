def excluding_vat_price(price: int) -> float:
    """ Calculate the original product price, without VAT. """
    return -1 if not price else round(price / 1.15, 2)
