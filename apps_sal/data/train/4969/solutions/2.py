def tower_builder(floors, xxx_todo_changeme):
    (w, h) = xxx_todo_changeme
    width = w * (2 * floors - 1)
    return [('*' * i).center(width) for i in range(w, width + 1, 2 * w) for _ in range(h)]
