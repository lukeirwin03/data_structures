class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data): # O(n)
        if data == self.data:
            return
        
        if data < self.data: # if data is less than the root
            # add to the left subtree
            if self.left: # if it is not a leaf node
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)

        if data > self.data: # if the data is greater than the root
            # add to the right subtree
            if self.right: # if it is not a leaf node
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def inorder_traversal(self): # O(n)
        elements = []

        if self.left: # visit left tree
            elements += self.left.inorder_traversal()

        elements.append(self.data) # visit root node

        if self.right: # visit right tree
            elements += self.right.inorder_traversal()

        return elements
    
    def post_order_traversal(self): # O(n)
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self): # O(n)
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def search(self, key): # O(logn)
        if self.data == key:
            return True
        
        if key < self.data: # key might be in the left subtree
            if self.left: # if not a leaf node
                return self.left.search(key) # recurse
            else:
                return False

        if key > self.data: # key might be in the right subtree
            if self.right: # if not a leaf node
                return self.right.search(key) # recurse
            else:
                return False
            
    def find_min(self):
        if self.left: # if there is a left subtree
            return self.left.find_min() 
        return self.data
        
    def find_max(self):
        if self.right: # if there is a right subtree
            return self.right.find_max()
        return self.data

    def calc_sum(self):
        sum = self.data

        if self.left: # if there is a left subtree
            sum += self.left.calc_sum() # calculate the sum of the left subtree

        if self.right: # if there is a right subtree
            sum += self.right.calc_sum() # calculate the sum of the right subtree

        return sum
    
    def delete(self, key):
        if key < self.data:
            if self.left: # if there is a left subtree
                self.left = self.left.delete(key)
        elif key > self.data:
            if self.right: # if there is a right subtree
                self.right = self.right.delete(key)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # --- using the right val --- #
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            # --- using the left val --- #
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements): # O(N)
    root = BSTNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 3, 4, 10, 23, 8, 15, 2, 17]
    bst = build_tree(numbers)
    bst.delete(4)
    print(bst.inorder_traversal())