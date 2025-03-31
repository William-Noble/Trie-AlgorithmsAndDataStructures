class node:
    def __init__(self, key):
        self.key = key # the value of the node, may not be necessary because the index of each node in its parent node can also be used as the key
        self.child = [None] * 26 # array of children, indexed from 0-25
        self.word_count = 1 # number of words attached to  a node, initialized to 1 because a node has 1 word when created
        self.word_end = False # indicated wether a node is a leaf node

class trie:
    def __init__(self): 
        self.root = node(None) # create a node with a null key to act as the root

    def insert(self, word):
        # code for inserting a new word, use node class when creating a new node, make sure the last node has word_end = True
        current_node = self.root # start the search at the root node
        if word.isalpha(): # ensure that all characters input belong to the alphabet
            word = word.lower() # convert to lowercase, very important because uppercase letters have a different ASCII number
            for letter in word: # iterate through the entire input of letters
                letter_index = ord(letter) - 97 # convert each letter to its ASCII equivalent and then shift by 97 so that a-z returns 0-25
                if current_node.child[letter_index] is not None: # check if the node has a child matching the input letter
                    current_node.word_count += 1
                    current_node = current_node.child[letter_index] # set the new current node to be that of the child matching the input letter
                else:
                    current_node.child[letter_index] = node(letter) # insert new node
                    current_node = current_node.child[letter_index] # move pointer to new node
            current_node.word_end = True
            return "Word inserted"
        else:
            return "Invalid input" # if the user gives an invalid input, exit immediately without searching

    def search(self, word):
        current_node = self.root # start the search at the root node
        if word.isalpha(): # ensure that all characters input belong to the alphabet
            word = word.lower() # convert to lowercase, very important because uppercase letters have a different ASCII number
            for letter in word: # iterate through the entire input of letters
                letter_index = ord(letter) - 97 # convert each letter to its ASCII equivalent and then shift by 97 so that a-z returns 0-25
                if current_node.child[letter_index] is not None: # check if the node has a child matching the input letter
                    current_node = current_node.child[letter_index] # set the new current node to be that of the child matching the input letter
                else:
                    return "Word not found" # if at any point the child does not match, immediately return not found and exit
            return "Word found" # if all letters exist in the tree, return word found
        else:
            return "Invalid input" # if the user gives an invalid input, exit immediately without searching
        
    def print(self): # not required for the project but is very useful for debugging
        self.print_recursive(self.root,0)

    def print_recursive(self,current_node,depth):
        for i in range(26):
            if current_node.child[25 - i] is not None:
                self.print_recursive(current_node.child[25 - i], depth+1)
            
        print("   |   " * depth + f"{current_node.key}, {current_node.word_count}, {current_node.word_end}")
            
            
trie = trie()
trie.insert("greet")
trie.insert("great")
trie.insert("greetings")
trie.insert("green")
trie.insert("grape")
word = input("Enter Word: ")
trie.insert(word)
trie.print()
