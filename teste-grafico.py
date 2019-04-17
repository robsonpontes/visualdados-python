# Visualização de dados em Python

import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7 ,9]
y1 = [2, 3, 7, 1, 0]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

tamanhoponto = [100,200,400,300,50]

titulo = "Grafico de Barras 2"
eixox = "Eixo x"
eixoy = "Eixo y"

#Titulo
plt.title(titulo)

# Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x1, y1, label = "Grupo 1", linestyle=":", color="#009900")
plt.scatter(x1, y1, label = "Grupo 2", color="r", marker=".", s=tamanhoponto)
plt.legend()


plt.show()
plt.savefig("figura.png", dpi=300)

