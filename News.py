import re


class News:
    title = ""
    body = ""
    id = 0

    def __init__(self, title, body, identity):
        self.id = identity
        self.title = title
        self.body = body
        self.title = self.title.lower()
        self.body = self.body.lower()
        self.puncRemove()
        self.stopWordRemove()

    def puncRemove(self):
        self.title = re.sub(r'[^\w\s]', ' ', self.title)
        self.body = re.sub(r'[^\w\s]', ' ', self.body)
        self.title = self.title.replace('\n', ' ')
        self.body = self.body.replace('\n', ' ')

    def stopWordRemove(self):
        f = open("stopwords.txt", "r")
        for line in f:
            for word in line.split():
                self.title = self.title.replace(' ' + word + ' ', ' ')
                self.body = self.body.replace(' ' + word + ' ', ' ')
