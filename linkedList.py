class Node:
    def __init__(self, data=None):
        """
        Initializes the node with the given data and sets the next node to None.

        :param data: the data to be stored in the node
        :type data: any
        """
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        """
        Initializes the class with a default value for the head attribute.
        """
        self.head = None

    def insert(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data: The data to be inserted into the new node.

        Returns:
            None
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            print(current_node.data)
            current_node = current_node.next_node
        current_node.next_node = new_node
        # # Assuming the task is to print the entire linked list
        # def print_list(self):
        #     """
        #     Prints out the data in each node of the linked list, starting from the head.
        #     """
        #     current_node = self.head
        #     while current_node:
        #         print(current_node.data)
        #         current_node = current_node.next_node

        # # Now calling the print_list method to print the result
        # my_linked_list.print_list()

my_linked_list = LinkedList()
my_linked_list.insert(1)
my_linked_list.insert(2)
my_linked_list.insert(3)
