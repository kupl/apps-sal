# pass in the linked list
# to access the head of the linked list
# linked_list.head
def search_k_from_end(linked_list, k):
    fast_index = 0
    slow = linked_list.head
    node = linked_list.head

    while fast_index < k:
        if node:
            node = node.next
            fast_index += 1
        else:
            return None

    while node:
        node = node.next
        slow = slow.next

    return slow.data
