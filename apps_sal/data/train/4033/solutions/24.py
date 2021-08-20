def contamination(text: str, char: str) -> str:
    return '' if text == '' or char == '' else char * len(text)
