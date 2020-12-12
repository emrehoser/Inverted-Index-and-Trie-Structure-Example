from Trie import Trie
import pickle
import json
import sys
trieResult = []

def dfs(node, prefix):
    if node.is_end:
        for id in node.documents:
            if id not in trieResult:
                trieResult.append(id)

    for child in node.children.values():
        dfs(child, prefix + node.char)
def query(word):
    if "*" not in word:
        with open('inverted_index.json', 'r') as input:
            dictInvertedIndex = json.load(input)

        print(dictInvertedIndex[word])

    else:
        word = word.replace("*", '')
        with open('trie_data.pickle', 'rb') as input:
            trieDataStructure = pickle.load(input)

        currentNode = trieDataStructure.root

        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return

        dfs(currentNode, word[:-1])

        print(trieResult)


string = sys.argv[1]
print(query(string))