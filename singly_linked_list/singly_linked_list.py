# Lists: 
    # 1. Store things in sequential order
    # 2. Allow us to index to fetch particular elements by index

# Linked Lists:
    # 1. Store things in sequential order
    # 2. Don't allow you to index

list = [5, 7, 3, 18, 22, 3] # This is kinda like a bookshelf

# Linked lists are kind of like chain? Each value is stored in it's own node

class Node:
    # it will have a value that the node is holding
    # and a reference to the next node in the linked list
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # method to the get the value of the node

    def get_value(self):
        return self.value

    # method to get the node's `next_node`
    def get_next(self):
        return self.next_node

    # method to update the node's `next_node` to the input node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None # Stores our first node in the list
        self.tail = None # Stores our end of the list
    
    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.set_next(new_node)

    def add_to_tail(self, value):
        # Create a node to add
        new_node = Node(value)
        # check if the Linked List is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        #otherwise, the list  has at least one node 
        else:
            # update the last node's `next_node` to the new node
            self.tail.set_next(new_node)
            #update `self.tail` to point to the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove value
            value = self.head.get_value() # this has to happen first so we can access the node we remove??
            self.head = None
            self.tail = None
            return value

        # otherwise, the linked list has more than one Node
        else:
        # store the last Node's value in another variable so we can return it
            value = self.tail.get_value()
        # we need to set `self.tail` to the second-to-last Node
        # the only way we can do this, is by traversing the whole linked list from the beginning

        # starting from the head, we'll traverse down to the second-to-last Node
        # init another reference to keep track of where we are in the linked list
        # as we're iterating
            current = self.head
            # keep iterating until the node after current is the tail? 
            while current.get_next() != self.tail:
                #keep iterating
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None)
            return value

    def remove_head(self):
        #check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
        # store the old head's value that we need to return
            value = self.head.get_value()
        # set `self.head` to the old head's `next_node`
            self.head = self.head.get_value()
        # return the old_head's value
            return value


# Stack: Last in, First Out
# Queue: First in, First Out

ll = LinkedList()
ll.add_to_tail(5)
#ll = Node(5)
#ll.add_to_end(7)
#ll.add_to_end(18)
#ll.add_to_end(22)

#ll.set_next(Node(7))
#ll.next_node.set_next(Node(18))
#ll.next_node_next.node.set_next(Node(22))