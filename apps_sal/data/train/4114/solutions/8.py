def pagination_text(page_number, page_size, total_products):
    s = min((page_number - 1) * page_size + 1, total_products)
    e = min(s + page_size - 1, total_products)
    return 'Showing {} to {} of {} Products.'.format(s, e, total_products)
