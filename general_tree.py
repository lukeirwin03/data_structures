class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self):
        if self.get_level() == 0:
            print(self.data)
        else:
            pre = self.get_level()* 3 * " " + "|__"
            print(pre + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Numbers")

    odd = TreeNode("Odd")
    odd_children = [1, 3, 5, 7, 9]
    for num in odd_children:
        odd.add_child(TreeNode(num))

    even = TreeNode("Even")
    even_children = [2, 4, 6, 8, 10]
    for num in even_children:
        even.add_child(TreeNode(num))

    root.add_child(odd)
    root.add_child(even)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()