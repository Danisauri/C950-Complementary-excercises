from BinarySearchTree import BinarySearchTree, BSTNode
from AVLTree import AVLTree, AVLNode

# FIXME Write function to determine the max depth of a tree
def relative_deep(tree, key):
    node = tree.root
    counter = 0
    while node is not None:
        if int(node.key) > int(key):
            counter +=1
            node = node.left
        elif int(node.key) < int(key):
            counter +=1
            node = node.right
        else:
            return counter
    return counter


def max_depth(node):
    if node is None:
        return 0
    else:
        left = max_depth(node.left)
        right = max_depth(node.right)
        if (left > right):
            return (left+1)
        else:
            return (right+1)


# Create empty tree objects
avl_tree = AVLTree()
binary_search_tree = BinarySearchTree()

# FIXME Read in random-looking integers separated by a space
#       and insert into trees as keys. Determine number
#       of comparisons per key and total number of comparisons
#       for the tree.

user_input = "47 19 3 12 18" # input()
total_comparison_avl = 0
total_comparison_bst = 0
for value in user_input.split():
    print("Key:", value)
    # AVL
    new_node = AVLNode(value)
    comparison = relative_deep(avl_tree, value)
    avl_tree.insert(new_node)
    avl_tree.rebalance(avl_tree.root)
    total_comparison_avl += comparison
    print("AVL - Insert comparisons:", comparison)

    # BST
    new_node = BSTNode(value)
    binary_search_tree.insert(new_node)
    comparison = relative_deep(binary_search_tree, value)
    total_comparison_bst += comparison
    print("BST - Insert comparisons:", comparison)
    print()




# FIXME Print max depth
print("Total # of comparisons")
print("AVL tree:", total_comparison_avl)
print("Binary search tree:", total_comparison_bst)
print()
print("Max tree depth")
print("AVL tree:",max_depth(avl_tree.root)-1)
print("Binary search tree",max_depth(binary_search_tree.root)-1)

# Print the tree after all inserts are complete
print('Trees after insertions:')
print('AVL tree', avl_tree)
print('\nBinary search tree', binary_search_tree)