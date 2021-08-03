def pagination_text(page_number, page_size, total_products):
    lower = (page_number - 1) * page_size + 1
    upper = min(total_products, page_number * page_size)
    return "Showing {} to {} of {} Products.".format(lower, upper, total_products)
