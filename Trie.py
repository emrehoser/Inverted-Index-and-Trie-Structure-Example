from Node import Node


class Trie(object):
    def __init__(self):
        self.root = Node('')

    def insert(self, word, documents):
        currentNode = self.root

        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                newNode = Node(char)
                currentNode.children[char] = newNode
                currentNode = newNode

        currentNode.is_end = True
        currentNode.documents = documents
