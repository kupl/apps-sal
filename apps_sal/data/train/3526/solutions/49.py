any_arrows = lambda arrows: any("damaged" not in arrow or not arrow["damaged"] for arrow in arrows)
