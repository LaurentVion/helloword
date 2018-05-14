import random
import math

#déclare la classe
class PiMonteCarlo:

    #constructeur
    def __init__(self, iteration):
        #attribut
        self.iteration = iteration

    #déclare une méthode
    def computePi(self):

        total = 0

        for i in range(1, self.iteration) :
            x = random.random()
            y = random.random()

            dist = math.sqrt(x * x + y * y)

            if dist <= 1:
                total = total + 1

        pi = total / self.iteration * 4

        return pi

#instancie la classe
myClass10 = PiMonteCarlo(10)
myClass1000 = PiMonteCarlo(1000)

pi10 = myClass10.computePi()
pi1000 = myClass1000.computePi()

print(pi10)
print(pi1000)

