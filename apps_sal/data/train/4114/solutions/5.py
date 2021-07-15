def pagination_text(page_number, page_size, total_products):
    start = (page_number - 1) * page_size + 1
    end = page_number * page_size
    if end > total_products:
        end = total_products
    return 'Showing {} to {} of {} Products.'.format(start, end, total_products)
