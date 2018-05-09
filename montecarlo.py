import random
import math

iteration = 10
total = 0


for i in range(1,iteration) :
    x = random.random()
    y = random.random()

    dist = math.sqrt(x * x + y * y)

    if dist <= 1:
        total = total + 1

# aire cercle = pi x r x r (ici r = 1)
# aire quart cercle = pi / 4
pi = total / iteration * 4

print(pi)
