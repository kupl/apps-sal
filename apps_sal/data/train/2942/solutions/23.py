def fold_to(distance): return None if distance < 0 else 0 if distance == 0 or __import__('math').log(distance * 10000, 2) < 0 else int(__import__('math').log(distance * 10000, 2)) + 1
