def pagination_text(page_number, page_size, total_products):
    start = (page_number - 1) * page_size + 1
    stop = min(start + page_size - 1, total_products)
    return 'Showing {} to {} of {} Products.'.format(start, stop, total_products)
