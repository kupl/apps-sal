def conference_picker(visited, offered):
    options = [c for c in offered if c not in visited]
    return options[0] if options else 'No worthwhile conferences this year!'
