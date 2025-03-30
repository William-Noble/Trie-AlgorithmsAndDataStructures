class node:
    def __init__(self, value, end = False):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None
        self.end = end

class Ternary_Trie:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if word.isalpha():
            word = word.lower()
            self.root = self.insert_recursive(self.root, word, 0)
        else:
            return "Invalid Input"

    def insert_recursive(self, current_node, word, i):
        if i < len(word):
            if current_node is None:
                current_node = node(word[i], i==len(word)-1)
                print(current_node.end)
            if current_node.value > word[i]:
                current_node.left = self.insert_recursive(current_node.left, word, i)
            elif current_node.value < word[i]:
                current_node.right = self.insert_recursive(current_node.right, word, i)
            else:
                current_node.middle = self.insert_recursive(current_node.middle, word, i+1)
        return current_node


    def search(self, word):
        current_node = self.root
        i = 0
        while True:
            if current_node is None or i >= len(word):
                return "Not Found"
            d = word[i]
            if current_node.end is True and i == len(word)-1 and current_node.value == d:
                return "Found"
            if d < current_node.value:
                current_node = current_node.left
            elif d > current_node.value:
                current_node = current_node.right
            else:
                i += 1
                current_node = current_node.middle

    def display(self): # not required for the project but is very useful for debugging
        self.display_recursive(self.root,0)

    def display_recursive(self,current_node,depth):
        if current_node:
            if current_node.right:
                self.display_recursive(current_node.right, depth+1)
            print(("   |   " * depth + f"{current_node.value, current_node.end}"))
            if current_node.middle:
                self.display_recursive(current_node.middle, depth+1)
            if current_node.left:
                self.display_recursive(current_node.left, depth+1)