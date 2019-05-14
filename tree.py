from anytree import Node, RenderTree


class BinaryTree:
    def __init__(self, left, right, data):
        self.right = right
        self.left = left
        self.data = data


class Tree:
    def __init__(self, children, data):
        self.children = children
        self.data = data

    def add_children(self, child):
        self.children.append(child)


if __name__ == '__main__':
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)

    print(udo)
    Node('/Udo')
    print(joe)
    Node('/Udo/Dan/Joe')

    for pre, fill, node in RenderTree(udo):
        print("%s%s" % (pre, node.name))
