class Node:

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.documents = []
        self.children = {}