def conference_picker(cv, co):
    return [[i for i in co if not i in cv] + ['No worthwhile conferences this year!']][0][0]
