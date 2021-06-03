"""
Author: Oliver Jan
Objective: Define a Linked List class to append, prepend, delete, insert, and print out the linked list
"""


class Node:
    number_of_nodes = 0

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        Node.number_of_nodes += 1

    @classmethod
    def delete(cls) -> None:
        Node.number_of_nodes -= 1


class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node

    def append(self, value):
        # find the last node where next_node is None and replace it's next_node with Node(value)
        dummy_node = self.head
        while True:
            if dummy_node.next_node is None:
                dummy_node.next_node = Node(value)
                break
            else:
                # if not None, go to the next node
                dummy_node = dummy_node.next_node
                continue

    def prepend(self, value):
        new_head_node = Node(value)
        dummy = self.head

        new_head_node.next_node = dummy
        self.head = new_head_node

    def delete_node(self, delete_position):
        # traverse along the linked list to position and delete that node
        dummy = self.head
        # if delete_position is 0, delete the head
        if delete_position == 0:
            print("Deleting the head")
            self.head = dummy.next_node
            Node.delete()

        if delete_position > Node.number_of_nodes:
            raise ValueError("Not enough nodes my guy")

        for i in range(1, delete_position+1):
            if i < delete_position:
                dummy = dummy.next_node
                continue
            elif i == delete_position:
                dummy.next_node = dummy.next_node.next_node
                Node.delete()

    @staticmethod
    def length_of_linked_list():
        return f"There are currently {Node.number_of_nodes} nodes in the linked list"

    def insert_node(self, insert_position: int, new_value):
        if insert_position == 0:
            self.prepend(new_value)

        if insert_position > Node.number_of_nodes:
            raise ValueError("Not enough nodes my guy")

        # set the dummy node to the head
        dummy = self.head

        for i in range(1, insert_position + 1):
            if i < insert_position:
                dummy = dummy.next_node
                continue
            elif i == insert_position:
                new_node = Node(new_value)
                new_node.next_node = dummy.next_node
                dummy.next_node = new_node
                break

    def print_linked_list(self):
        dummy_node = self.head
        print(f"{dummy_node.value} -> ", end='')
        while True:
            if dummy_node.next_node is None:
                break
            else:
                print(f"{dummy_node.next_node.value} -> ", end='')
                dummy_node = dummy_node.next_node
        print("None")

    def search_linked_list(self, value):
        dummy = self.head
        for i in range(0, Node.number_of_nodes):
            if dummy.value == value:
                print(f"{value} was found!")
                return value
            else:
                dummy = dummy.next_node

        print(f"{value} was not found! Try again next time.")

    def is_empty(self) -> bool:
        # check if the linked list is empty
        if self.head is None:
            return True
        else:
            return False


if __name__ == '__main__':
    head = Node(1)
    linked_list = LinkedList(head)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list.append(10)
    linked_list.insert_node(5, 20)
    linked_list.insert_node(8, 5)
    linked_list.print_linked_list()
    print(linked_list.length_of_linked_list())
    linked_list.delete_node(8)
    linked_list.insert_node(8, 5)
    linked_list.delete_node(8)
    linked_list.print_linked_list()
    print(linked_list.length_of_linked_list())
    linked_list.delete_node(0)
    linked_list.print_linked_list()
    print(linked_list.length_of_linked_list())
    linked_list.insert_node(0, "NEW HEAD")
    linked_list.print_linked_list()
    print(linked_list.length_of_linked_list())
    linked_list.search_linked_list(5)

    # Testing if is_empty() works
    empty_linked_list = LinkedList()
    print(empty_linked_list.is_empty())
