def repeat_it(string, n):
    if isinstance(string, int) or isinstance(string, float) or isinstance(string, dict) or isinstance(string, list):
        return "Not a string"
    return string * n
