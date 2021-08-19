from typing import Union


def quote(fighter: str) -> Union[str, None]:
    fighter = fighter.casefold()
    if fighter == 'george saint pierre':
        return 'I am not impressed by your performance.'
    elif fighter == 'conor mcgregor':
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    return None
