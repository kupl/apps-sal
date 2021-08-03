def pagination_text(p, sz, total):
    return 'Showing ' + str((p - 1) * sz + 1) + ' to ' + str(total if p * sz > total else p * sz) + ' of ' + str(total) + ' Products.'
