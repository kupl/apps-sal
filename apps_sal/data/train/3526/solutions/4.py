any_arrows=lambda arrows: any([not x["damaged"] if "damaged" in x else True for x in arrows])
