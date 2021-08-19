def list_to_array(lst):
    return [lst.value] + list_to_array(lst.next) if lst else []
