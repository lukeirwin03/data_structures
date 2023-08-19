"""
- Inserting doesn't require you to change the memory location of every other element after the inserted value
- Linked list traversal = O(n)
- Accessing Element by Value = O(n)
- Insert/Delete First Value = O(1)
- Insert/Delete Last Value = O(N)

memory locations:          0x0050           0x00A1           0x00C5           0x00C0
singly_linked_list = {     [298, 0x00A1] -> [305, 0x00C5] -> [301, 0x00C0] -> [292, null]    }
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data): # O(1)
        self.head = Node(data, self.head) # set the first value equal to a new node
    
    def insert_at_end(self, data): # O(n)
        if self.head is None: # if the list is empty
            self.head = Node(data, None) # set the head to the new value
            return
        
        current = self.head # for iterating
        while current.next: # while the next value is not None (while the current value is not the last value)
            current = current.next # iterate

        current.next = Node(data, None) # add a new node after the current(last) node

    def insert_values(self, data_list): # O(n)
        self.head = None
        for value in data_list: # for each value in data_list
            self.insert_at_end(value) # add the value to the end

    def length(self): # O(n)
        count = 0
        current = self.head # for iterating
        while current: # while the current value is not None
            count += 1 # add 1 to the count
            current = current.next # iterate
        return count

    def remove_at(self, index): # O(n)
        if index < 0 or index >= self.length(): # if the index is invalid
            raise Exception("Invalid index") # raise an exception
        
        if index == 0: # if the index is the head
            self.head = self.head.next # remove the head
            return
        
        current = self.head # for iterating
        while index > 1: # while we are not at the node index previous to the one we are trying to remove
            current = current.next # iterate
            index -= 1 # update index
        
        current.next = current.next.next # replace the next node with the node after that

    def insert_at(self, index, data): # O(n)
        if index < 0 or index > self.length(): # if the index is invalid
            raise Exception("Invalid index") # raise an exception
        
        if index == 0: # if the index is the head
            self.insert_at_beginning(data) # insert at beginning
            return
        
        if index == self.length() - 1: # if the index is the tail
            self.insert_at_end(data) # insert at end
            return

        current = self.head # for iterating
        while index > 1: # while we are not at the node index previous to the location where we are trying to add
            current = current.next # iterate
            index -= 1 # update index
        
        current.next = Node(data, current.next) # the next node becomes a new node

    def print(self): # O(n)
        if self.head is None: # if the list is empty
            print("List is Empty")
            return
        
        current = self.head # for iterating
        linked_list_string = ''

        while current: # while the current node is not 
            linked_list_string += str(current.data) 
            if(current.next): # if the current value is not the last value
                linked_list_string += ' -> '
            current = current.next # iterate

        
        print(linked_list_string)