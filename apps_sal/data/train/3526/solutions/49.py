def any_arrows(arrows): return any("damaged" not in arrow or not arrow["damaged"] for arrow in arrows)
