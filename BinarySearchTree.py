class LeafNode():
    """A class representation of a leaf node on a binary search tree"""
    
    def __init__(self, value: int = None) -> None:
        self.value : int = value
        self.leftChild : LeafNode = None
        self.rightChild : LeafNode = None
 

class BinaryTree():
    """A class representation of a binary search tree"""
    def __init__(self) -> None:
        BinaryTree.root = LeafNode(None)

    def insert(self, key : int) -> None:
        if self.root.value == None:
            self.root.value = key
            return
        
        subtreeRoot = self.root
        prev = None
        
        
        while subtreeRoot != None:        
            prev = subtreeRoot
            if key < subtreeRoot.value:
                subtreeRoot = subtreeRoot.leftChild
            else:
                subtreeRoot = subtreeRoot.rightChild
                        
        if key < prev.value:
            prev.leftChild = LeafNode(key)
            #print(f"{prev.value} left {key}")
        else:
            prev.rightChild = LeafNode(key)
            #print(f"{prev.value} right {key}")

    def height(self, index) -> int:
        if self.root.value == None:
            return 0
        elif index == None:
            return 0
        else:
            leftHeight = self.height(index.leftChild)
            rightHeight = self.height(index.rightChild)
            
            if leftHeight > rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1


    def inorderTraversal(self, index) -> None:
        if self.root.value == None:
            print("The tree is empty.")

        elif index == None:
            return
        
        else:
            
            self.inorderTraversal(index.leftChild)
            print(index.value, end=" ")
            self.inorderTraversal(index.rightChild)

    
       

def main():
    tree = BinaryTree()
    
    
    #To get these values, I rolled a d100 10 times
    tree.insert(37)
    tree.insert(49)
    tree.insert(84)
    tree.insert(8)
    tree.insert(72)
    tree.insert(21)
    tree.insert(40)
    tree.insert(25)
    tree.insert(13)
    tree.insert(57)
    

    print(f"Binary Tree Height: {tree.height(tree.root)}")
    
    print(f"In-Order Traversal: ", end="")
    tree.inorderTraversal(tree.root)
    print("\n")
        
if __name__ == "__main__": main()
    
