def roof_fix(new, old):
    return all((patch == ' ' for (patch, tile) in zip(new, old) if tile in '\\/'))
