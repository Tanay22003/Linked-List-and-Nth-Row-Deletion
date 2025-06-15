class Node:
    """A Node in a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements in the linked list"""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        if not self.head:
            print("Error: Cannot delete from an empty list.")
            return

        if n <= 0:
            print("Error: Index must be a positive integer.")
            return

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            print("Error: Index out of range.")
            return

        current.next = current.next.next


# ======= Test the LinkedList Implementation =======
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()

    # Append data to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

    print("Original List:")
    ll.print_list()

    # Delete 3rd node
    ll.delete_nth_node(3)
    print("\nAfter deleting 3rd node:")
    ll.print_list()

    # Delete 1st node
    ll.delete_nth_node(1)
    print("\nAfter deleting 1st node:")
    ll.print_list()

    # Try deleting node with invalid index
    ll.delete_nth_node(10)  # Should show error

    # Try deleting from an empty list
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)  # Should show error
