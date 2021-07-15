def monty_hall(cdoor, pguesses):
    pick_cdoor=1-pguesses.count(cdoor)/len(pguesses)
    return round(pick_cdoor*100)

