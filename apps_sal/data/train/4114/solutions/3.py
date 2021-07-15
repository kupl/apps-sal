def pagination_text(page_number, page_size, total_products):
  return "Showing %d to %d of %d Products." % (
      page_size * (page_number - 1) + 1,
      min(total_products, page_size * page_number),
      total_products)

