def excluding_vat_price(price):
    """
    Calculate price before VAT
    """
    return round(price / 1.15, 2) if isinstance(price, float) or isinstance(price, int) else -1
