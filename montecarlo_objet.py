import random
import math

#déclare la classe
class PiMonteCarlo:

    #déclare une méthode
    def computePi(self, iteration):

        total = 0

        for i in range(1,iteration) :
            x = random.random()
            y = random.random()

            dist = math.sqrt(x * x + y * y)

            if dist <= 1:
                total = total + 1

        pi = total / iteration * 4

        return pi

#instancie la classe
myClass = PiMonteCarlo()

pi10 = myClass.computePi(10)
pi1000 = myClass.computePi(1000)

print(pi10)
print(pi1000)

