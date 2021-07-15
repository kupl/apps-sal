def conference_picker(visited, offered):
    return [city for city in (offered + ["No worthwhile conferences this year!"]) if city not in visited][0]
