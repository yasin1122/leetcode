"""
def append(self, value):
    # Create a new node with the given value
    new_node = Node(value)
 
    # Check to see if the linked list is empty
    if self.head is None:
        # Point both head and tail at the new node
        self.head = new_node
        self.tail = new_node
    else:
        # Point the next pointer of the last node at the new node
        self.tail.next = new_node
        # Point tail at the new node
        self.tail = new_node
 
    # Increment the length of the linked list
    self.length += 1
"""