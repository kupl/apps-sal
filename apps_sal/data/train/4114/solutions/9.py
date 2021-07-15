def pagination_text(page_number, page_size, total_products):
    start = (page_number-1)*page_size+1
    end = total_products if page_number*page_size > total_products else page_number*page_size
    li = ['Showing',str(start),'to',str(end),'of',str(total_products),'Products.']
    return ' '.join(li)
