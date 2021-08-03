def tower_builder(n, xxx_todo_changeme):
    (w, h) = xxx_todo_changeme
    return [str.center("*" * (i * 2 - 1) * w, (n * 2 - 1) * w) for i in range(1, n + 1) for _ in range(h)]
