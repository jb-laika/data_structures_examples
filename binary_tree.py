class BTNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return "<" + str(self.data) + ">"

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_root(self):
        return self.parent is None


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def search(self, target):
        if self.root is None:
            return False
        return self.search_at_node(self.root, target)

    def search_at_node(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        if not node.left is None and self.search_at_node(node.left, target):
            return True
        if not node.right is None:
            return self.search_at_node(node.right, target)
        return False

    def insert(self, data):
        if self.search(data):
            return False
        elif self.root is None:
            self.root = BTNode(data)
        else:
            node = BTNode(data)
            self.insert_at_node(self.root, node)

    def insert_at_node(self, current_node, node):
        if node.data > current_node.data:
            if current_node.right is None:
                node.parent = current_node
                current_node.right = node
            else:
                self.insert_at_node(current_node.right, node)
        elif node.data < current_node.data:
            if current_node.left is None:
                node.parent = current_node
                current_node.left = node
            else:
                self.insert_at_node(current_node.left, node)

    def height(self):
        if self.root is None:
            return None
        else:
            node = self.root
            return self.max_dist_to_leaf(node) - 1

    def max_dist_to_leaf(self, node):
        if node is None:
            return False
        return max(self.max_dist_to_leaf(node.left), self.max_dist_to_leaf(node.right)) + 1


def create_subtree(root, left_list, right_list, parent):
    temp = BTNode(root)
    temp.parent = parent
    if len(left_list) == 0:
        temp.left = None
    else:
        temp.left = create_subtree(left_list[0], left_list[1], left_list[2], temp)
    if len(right_list) == 0:
        temp.right = None
    else:
        temp.right = create_subtree(right_list[0], right_list[1], right_list[2], temp)
    return temp


# reads from nested list representation of trees
def list_to_tree(tlist):
    tree = BinaryTree()
    tree.root = create_subtree(tlist[0], tlist[1], tlist[2], None)
    return tree


def print_node_info(subtree, level):
    if subtree is None:
        return
    print('Node:', subtree.data, 'Level:', level, 'Parent:', subtree.parent)
    print_node_info(subtree.left, level + 1)
    print_node_info(subtree.right, level + 1)


'''
Test case 1 asserts that an empty binary tree returns a height of 0.
Test case 2 asserts that a binary tree of height 4 returns its height properly.
Test case 2 asserts that a binary tree of height 1 returns its height properly.
'''


def test_height_1():
    bst = BinaryTree()
    assert bst.height() is None, "expected height is None, height returned is " + str(bst.height())


def test_height_2():
    bst = list_to_tree([30,
                        [20,
                         [10, [], []],
                         [25, [23, [], []], [27, [], []]]],
                        [40, [], []]])
    assert bst.height() == 3, "expected height is 3, height returned is " + str(bst.height())


def test_height_3():
    bst = BinaryTree()
    bst.insert(3)
    assert bst.height() == 0, "expected height is 0, height returned is " + str(bst.height())

