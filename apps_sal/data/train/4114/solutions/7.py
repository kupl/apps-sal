def pagination_text(page_number, page_size, total_products):
    fr = page_number * page_size - page_size + 1
    to = min(fr + page_size - 1, total_products)
    return "Showing %d to %d of %d Products." % (fr, to, total_products)
