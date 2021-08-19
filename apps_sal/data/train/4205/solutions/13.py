from typing import Dict


def cannons_ready(gunners: Dict[str, str]) -> str:
    """ If all answers from gunners are 'aye' then `Fire!` if one or more are 'nay' then `Shiver me timbers!` """
    gunners_orders = {True: 'Fire!', False: 'Shiver me timbers!'}
    return gunners_orders.get(len(list(filter(lambda _: _ == 'aye', gunners.values()))) == len(gunners))
