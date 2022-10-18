#añadir
#buscar
#print

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.add_val(val, self.root)

    def add_val(self, val, node):
        if val < node.v:
            if node.l is not None:
                self.add_val(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self.add_val(val, node.r)
            else:
                node.r = Node(val)
    
    def search(self, val):
        if self.root is not None:
            return self.search_val(val, self.root)
        else:
            return None

    def search_val(self, val, node):
        if val == node.v:
            return node.v
        elif (val < node.v and node.l is not None):
            return self.search_val(val, node.l)
        elif (val > node.v and node.r is not None):
            return self.search_val(val, node.r)

    def print_tree(self):
        if self.root is not None:
            self.print_all(self.root)

    def print_all(self, node):
        if node is not None:
            self.print_all(node.l)
            print(str(node.v) + ' ')
            self.print_all(node.r)
    

tree = Tree()
tree.add(10)
tree.add(7)
tree.add(15)
tree.add(2)
tree.add(4)

print(tree.print_tree())
