def hero(bullets, dragons):
    """
    Dadas una cantidad de balas <bullets> y una cantidad de dragones <dragons>,
    devueve con True o False si esa cantidad de balas puede matar a esa cantidad de dragones.
    El numero necesario para matar un dragon son dos balas.
    """
    if bullets >= 2 * dragons:
        return True
    else:
        return False
