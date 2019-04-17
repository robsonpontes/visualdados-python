#box plot

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    numero_aleatorio = random.randint(0,20)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Box Plot");
plt.show()