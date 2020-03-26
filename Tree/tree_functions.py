# We can represent trees in python by nested lists.
# Datum is the value of given tree's root node
# Left is left child. It can be None, leaf node or a tree.
# Same for right.


def datum(tree):
    return tree[0]


def left(tree):
    return tree[1]


def right(tree):
    return tree[2]

def children(tree):
    return tree[1:]

def traverse_children(tree):
    i = 0
    children_list = tree[1:]
    while i < len(children_list):


def isempty(tree):
    return tree == []


def createnode(create_datum, left_child=None, right_child=None):
    return [create_datum,
            left_child if left_child else [],
            right_child if right_child else []]


# Now we will consider about traversal types.
# Pre-order traversal is traversing ROOT-LEFT-RIGHT.
# In-order traversal is traversing LEFT-ROOT-RIGHT.
# Post-order traversal is traversing LEFT-RIGHT-ROOT.
# Level-order traversal is traversing ROOT-LEFT to RIGHT.
# This left to right statement is traversing on same level.


def preorder_traverse(tree):
    if isempty(tree):
        return
    print(datum(tree))
    preorder_traverse(left(tree))
    preorder_traverse(right(tree))


def inorder_traverse(tree):
    if isempty(tree):
        return
    inorder_traverse(left(tree))
    print(datum(tree))
    inorder_traverse(right(tree))


def postorder_traverse(tree):
    if isempty(tree):
        return
    inorder_traverse(left(tree))
    inorder_traverse(right(tree))
    print(datum(tree))


def levelorder_traverse(tree):
    if isempty(tree):
        return
    print(datum(tree))
    levelorder_traverse(datum(tree[1]))
    levelorder_traverse(datum(tree[2]))


# Let's write some codes about specific trees


def binary_search_tree(elem, tree):
    if isempty(tree):
        return False
    if elem == datum(tree):
        return True
    elif elem < datum(left(tree)):
        binary_search_tree(elem, left(tree))
    elif elem > datum(left(tree)):
        binary_search_tree(elem, right(tree))


def insert_node(elem, tree):  # Inserts a node in binary search tree.
    if isempty(tree):         # If tree is empty, creates a tree.
        tree.extend(createnode(elem))
    if elem == datum(tree):
        return
    elif elem < datum(tree):
        insert_node(elem, left(tree))
    elif elem > datum(tree):
        insert_node(elem, right(tree))
