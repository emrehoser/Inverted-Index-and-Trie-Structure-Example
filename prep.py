from html.parser import HTMLParser
import News
from Trie import Trie
import pickle
import json
from Node import Node

newsArray = []
dictInvertedIndex = {}
trieDataStructure = Trie()



class MyParser(HTMLParser):
    startTag = ""
    endTag = ""
    newsTitle = ""
    newsStory = ""
    newsId = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'reuters':
            for attr in attrs:
                if attr[0] == 'newid':
                    self.newsId = attr[1]

        if tag == 'title' or tag == 'body':
            self.startTag = tag

    def handle_endtag(self, tag):
        if tag == 'reuters':
            news = News.News(self.newsTitle, self.newsStory, self.newsId)
            newsArray.append(news)
            self.newsTitle = ""
            self.newsStory = ""
            self.newsId = 0

    def handle_data(self, data):
        if self.startTag == 'title':
            self.newsTitle = data
            self.startTag = ""
        if self.startTag == 'body':
            self.newsStory = data
            self.startTag = ""


parser = MyParser()

for x in range(0, 22):
    if x < 10:
        f = open("reut2-00" + str(x) + ".sgm", "r", encoding="latin1")
        parser.feed(f.read())
        f.close()
    else:
        f = open("reut2-0" + str(x) + ".sgm", "r", encoding="latin1")
        parser.feed(f.read())
        f.close()

dict = {}

for article in newsArray:
    for word in article.title.split():
        if word not in dict:
            dict[word] = []
        if word in dict:
            if article.id not in dict[word]:
                dict[word].append(article.id)
    for word in article.body.split():
        if word not in dict:
            dict[word] = []
        if word in dict:
            if article.id not in dict[word]:
                dict[word].append(article.id)

with open('inverted_index.json', 'w') as output:
    json.dump(dict, output)

trie = Trie()

for word in dict:
    trie.insert(word, dict[word])

with open('trie_data.pickle', 'wb') as output:
    pickle.dump(trie, output)




