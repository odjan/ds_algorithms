
class Node:
    
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class Queue:

    """
    I know there is a deque collection in python I can use, but I want to derive this from scratch
    1
    2 <- 1 (enqueue 2)
    3 <- 2 <-1 (enqueue 3)
    3 <- 2 (dequeue 1)
    """

    nodes_in_queue = 0

    def __init__(self, head=None):
        if head is None:
            self.head = None
        else:
            self.head = Node(head)
            self.nodes_in_queue += 1
    

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


    def get_front(self):
        if self.head is None:
            print("No front of the line for empty queue")
            return

        dummy = self.head
        for i in range(self.nodes_in_queue-1):
            dummy = dummy.next_node
        print(f"The value in front is {dummy.value}")


    def get_back(self):
        if self.head is not None:
            print(f"The value in the back is {self.head.value}")
        else:
            print("No back of the line for empty queue")


    def enqueue(self, value):
        if value is None:
            return f"No valid value"
        
        dummy = self.head
        new_head = Node(value)
        new_head.next_node = dummy
        self.head = new_head
        self.nodes_in_queue += 1


    def dequeue(self):
        if self.nodes_in_queue == 0:
            print("Empty queue")
            return

        if self.nodes_in_queue == 1:
            self.head = None
            print("Last element dequeued. There is now an empty queue")
            self.nodes_in_queue -= 1
            return
        
        dummy = self.head
        for i in range(1, self.nodes_in_queue-1):
            dummy = dummy.next_node
            print(dummy.value)
        
        print(f"{dummy.next_node.value} is being deqeued")
        dummy.next_node = None
        self.nodes_in_queue -= 1
        print(f"There are now {self.nodes_in_queue} nodes left")

    
# Driver code    
if __name__ == "__main__":
    new_queue = Queue(10)
    new_queue.get_front()
    new_queue.enqueue(20)
    new_queue.enqueue(30)
    new_queue.enqueue(40)
    new_queue.get_front()
    new_queue.get_back()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.get_back()
    new_queue.get_front()





    
