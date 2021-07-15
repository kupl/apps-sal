def cookie(x):
    return f"Who ate the last cookie? It was {'the dog' if isinstance(x, bool) else 'Zach' if isinstance(x, str) else 'Monica'}!"
