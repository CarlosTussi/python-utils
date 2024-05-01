import random

class BinaryTree():

    def __init__(self):
        self.root = None
    

    class Node():

        def __init__(self, key, data, right = None, left = None):
            self.key = key
            self.data = data
            self.left_child = left
            self.right_child = right

        def __str__(self):
            return f"K({self.key})-V({self.data})"

    def set_root(self, key, data):
        self.root = self.Node(key, data)
    

    """
    EXTRACT MINIMUM VALUE

    Smallest value bigger than the key we are removing
    """
    def extract_minimum(self, current_node = None, parent_node = None) -> Node:
        if current_node is None:
            current_node = self.root
        
        if(current_node.left_child is None):
            #Removes the link between the parent and the minimum child as this child is gonna be the new root of the subtree
            if(parent_node is not None):
                parent_node.left_child = None
            return current_node
        elif(current_node.left_child is not None):
            parent_node = current_node
            return self.extract_minimum(current_node.left_child, parent_node)


    """
    INSERTING
    """
    def insert_node(self, key, data, current_node = None):
        if (not current_node):
            current_node = self.root

        #Key > current root => check right child
        if(key > current_node.key):
            #If current root is NOT a leaf
            if(current_node.right_child):
                self.insert_node(key, data, current_node.right_child)
                #If current root is a leaf
            else:
                current_node.right_child = self.Node(key, data)
        #Key < current root => check left child
        elif(key < current_node.key):
            #If current root is NOT a leaf
            if(current_node.left_child):
                self.insert_node(key, data, current_node.left_child)
            #If current root is a leaf
            else:
                current_node.left_child = self.Node(key, data)
                
        if(key == current_node.key):
            print("Error - Keys cannot be duplicated")

    """
    REMOVING

    Remove by promoting the smallest key from the subtree bigger than the node we want to remove

    """
    def remove_node(self, key, current_node = None, parent_node = None):
        if(current_node is None):
            current_node = self.root

        #
        # Node to be deleted found
        #
        if(key == current_node.key):
            #Node has no right_child. 
            if(current_node.right_child is None):       #Right_child to comply with the "smallest key from the subtree root BIGGER than the current node"
                if(current_node.key > parent_node.key):
                    parent_node.right_child = current_node.left_child
                else:
                    parent_node.left_child = current_node.left_child

            #Not a leaf node
            else:
                #Find the smallest key from the subtree with root bigger than the current node.
                min_node = self.extract_minimum(current_node.right_child)   #Right_child to comply with the "smallest key from the subtree root BIGGER than the current node"
                
                #Link parent with new subtree root
                if(min_node.key < parent_node.key):
                    parent_node.left_child = min_node
                elif(min_node.key > parent_node.key):
                    parent_node.right_child = min_node
                
                #Link rest of the tree with the subtree with the new root
                min_node.left_child = current_node.left_child
                min_node.right_child = current_node.right_child
   
        #
        # Recursive call: finding the node to be removed
        #
        else:
            if(key > current_node.key):
                #Recursion right
                if(current_node.right_child is not None):
                    parent_node = current_node
                    self.remove_node(key, current_node.right_child, parent_node)
                else:
                    print(f"Element {key} does not exist")
                pass
            elif(key < current_node.key):
                #Recursion left
                if(current_node.left_child is not None):
                    parent_node = current_node
                    self.remove_node(key, current_node.left_child, parent_node)
                else:
                    print(f"Element {key} does not exist")   

    """
    SEARCHING
    """
    def search_node(self, key, current_node = None):
        if(current_node is None):
            current_node = self.root

        #Node key is found
        if(current_node.key == key):
             return current_node.data
        #Recursion right subtree
        if(key > current_node.key):
            if(current_node.right_child is not None):
                return self.search_node(key, current_node.right_child)
            else:
                return "Element not found"
        #Recursion left subtree
        elif(key < current_node.key):
            if(current_node.left_child is not None):
                return self.search_node(key, current_node.left_child)
            else:
                return "Element not found"
    """
    TRAVESRSE IN ORDER
    Left-Root-Right
    """
    def traverse_in_order(self, current_node = None):
        if(current_node is None):
            current_node = self.root
        
        if(current_node.left_child is None):
            print(f"{current_node.key}", end = " ")
            if(current_node.right_child is not None):
                self.traverse_in_order(current_node.right_child)
        else:
            self.traverse_in_order(current_node.left_child)
            print(f"{current_node.key}", end = " ")
            if(current_node.right_child is not None):
                self.traverse_in_order(current_node.right_child)

    """
    TRAVERSE PRE ORDER
    Root-Left-Right
    """
    def traverse_pre_order(self, current_node = None):
        if(current_node is None):
            current_node = self.root
        
        print(f"{current_node.key}", end =" ")
        if(current_node.left_child is not None):
            self.traverse_pre_order(current_node.left_child)
        if(current_node.right_child is not None):
            self.traverse_pre_order(current_node.right_child)


    """
    TRAVERSE POST ORDER
    Left-Right-Root
    """
    def traverse_post_order(self, current_node = None):
        if(current_node is None):
            current_node = self.root
        
        #Leaf
        if(current_node.left_child is None and current_node.right_child is None):
            print(current_node.key, end = " ")
        #Not a Leaf
        else:
            if(current_node.left_child is not None):
                self.traverse_post_order(current_node.left_child)
            if(current_node.right_child is not None):
                self.traverse_post_order(current_node.right_child)
            print(current_node.key, end = " ")

            

        

if __name__ == "__main__":
    NODES = [10,20,15,9,8,13,25,60,65,63,67,70,90,75,81]
    tree = BinaryTree()
    tree.set_root(50, "My root") 

    for new_node in NODES:
        tree.insert_node(new_node, "Payload: "+str(new_node))

    print("Traverse In-Order: ", end = "")
    tree.traverse_in_order()
    print()

    print("Traverse Pre-Order: ", end = "")
    tree.traverse_pre_order()
    print()

    print("Traverse Post-Order: ", end = "")
    tree.traverse_post_order()
    print()