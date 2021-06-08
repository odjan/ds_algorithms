
class Node:
    
    def __init__(self, value):
        self.value = value
        self.next_node = None

class Stack:

    """
    A stack is a data structure that follows the LIFO (last in, first out) order
    with two main insert and delete functions, push and pop

    Push appends a new node to the top of the stack -> O(1) as the top node is always known
    Pop removes the top node at the top of the stack -> O(1) as the top node is always known
    """
    stack_height = 0

    def __init__(self, head=None):
        if head is not None:
            self.head = Node(head)
            self.stack_height += 1
        else:
            # case for when no value is provided
            self.head = head


    def peek(self):
        # returns the top node's value
        if self.head: 
            return f"Top value of stack object is {self.head.value}"
        else:
            return None
        

    def push(self, value):
        """
        Args:
            value (int): value of node being pushed onto the top of the stack
        """
        # for an empty stack
        if self.stack_height == 0:
            self.head = Node(value)
            self.stack_height += 1
            return

        # for any height stack, we want the pushed value to become the new head, 
        # with pointer to the prior head
        new_head = Node(value)
        prior_head = self.head
        self.head = new_head
        self.head.next_node = prior_head
        self.stack_height += 1

    def pop(self):
        """
        Pop will remove the lastly pushed node of the stack
        """
        if self.head: 
            print(f"Node value of {self.head.value} will be popped")
            popped_head = self.head
            self.head = popped_head.next_node
            self.stack_height -= 1
        else:
            print("No more items to pop!")

    def print_stack(self):
        if self.stack_height == 0:
            print("Nothing in the stack my guy")
            return

        dummy = self.head
        print("Top: ", end="")
        print(f"{dummy.value}", end="<-")
        for i in range(1, self.stack_height):
            if dummy.value is not None:
                print(f"{dummy.next_node.value}", end="<-")
                dummy = dummy.next_node
            else:
                print("No items in stacks")
        print("Bottom of Stack")

    
if __name__ == "__main__":

    new_stack = Stack(20)
    new_stack.push(30)
    new_stack.push(40)
    new_stack.push(50)
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    print(new_stack.peek())
