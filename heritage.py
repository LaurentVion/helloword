class Document:

    def __init__(self, titre):
        self.titre = titre

class Livre(Document):

    def __init__(self, titre, nbpage):
        Document.__init__(self, titre)
        self.nbpage = nbpage

    def __str__(self):
        return "Livre {0} nbpage = {1}".format(self.titre, self.nbpage)

class DVD(Document):

    def __init__(self, titre, duration):
        Document.__init__(self, titre)
        self.duration = duration

    def __str__(self):
        return "DVD {0} duration = {1}".format(self.titre, self.duration)


biblioteque = [ Livre('livre1', 15), DVD('dvd1', 66)]

for doc in biblioteque:
    print(doc)
