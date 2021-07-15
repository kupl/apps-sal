from typing import Dict

def cannons_ready(gunners: Dict[str,str]) -> str:
    """Returns fire if all gunners are ready else shiver me timbers."""
    ready = not 'nay' in gunners.values()
    return 'Fire!' if ready else 'Shiver me timbers!'
