import urllib2
from HTMLParser import HTMLParser

content = urllib2.urlopen("https://fr.wikipedia.org/wiki/Python_(langage)").read()

class MyParser(HTMLParser):

    def __init__(self):

        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs).get('href'))

p = MyParser()
p.feed(content)
print p.links

