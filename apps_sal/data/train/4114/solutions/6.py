def pagination_text(page_number, page_size, total_products):
    return 'Showing {} to {} of {} Products.'.format((page_number - 1) * page_size + 1, min(page_number * page_size, total_products), total_products)
