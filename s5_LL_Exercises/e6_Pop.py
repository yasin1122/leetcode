def pop(self):
    # Check if the list is empty
    if self.length == 0:
        return None
    # Initialize temp and pre to the head
    temp = self.head
    pre = self.head
    # Iterate until the last node
    while(temp.next):
        pre = temp
        temp = temp.next
    # Set the new tail to the previous node
    self.tail = pre
    # Remove link to the removed node
    self.tail.next = None
    # Decrement list length by 1
    self.length -= 1
    # Check if the list is now empty
    if self.length == 0:
        # Set head and tail to None
        self.head = None
        self.tail = None
    # Return the removed node
    return temp