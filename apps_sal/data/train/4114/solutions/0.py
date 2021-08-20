def pagination_text(page_number, page_size, total_products):
    first = page_size * (page_number - 1) + 1
    last = min(total_products, first + page_size - 1)
    return 'Showing %d to %d of %d Products.' % (first, last, total_products)
