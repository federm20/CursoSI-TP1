import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random


# dimension VC de un triangulo
def act1_a1():
    # dibuja puntos
    plt.plot(3.5, 5, 5, 8, 6.5, 5, marker='o', c='red')
    plt.plot(4.5, 3, 4, 7, 5.5, 3, 6, 7, marker='o', c='green')

    # dibuja clasificador (triangulo)
    plt.plot([3.3, 6.7, 5, 3.3], [4.8, 4.8, 8.2, 4.8], c='black')

    plt.title("Dimensión VC Triángulo")
    plt.legend(loc=2)
    plt.show()


# dimensión VC de un hiperplano en 3D
def act1_a2():
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    # dibuja puntos
    ax1.scatter(0, 0, 6, marker='o', c='red')
    ax1.scatter(9, 9, -12, marker='o', c='red')
    ax1.scatter(9, 9, 6, marker='o', c='green')
    ax1.scatter(0, 0, -12, marker='o', c='green')

    # define hiperplano y dibuja
    normal = np.array([1, 1, 1])
    point = np.array([1, 2, 3])
    d = -point.dot(normal)

    # crea x,y
    xx, yy = np.meshgrid(range(10), range(10))

    # calcula z
    z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

    ax1.plot_wireframe(xx, yy, z)

    plt.title("Dimensión VC Hiperplano")
    plt.show()


# clasificador rectangular
def act1_b():
    # crea 60 datos aleatorios de cada clase
    N = 60

    dataset = []
    g1 = {'x1': None, 'x2': None, 'y1': None, 'y2': None}
    g2 = {'x1': None, 'x2': None, 'y1': None, 'y2': None}

    # crea datos aleatorios de dos clases diferentes
    for i in range(N):
        dataset.append((0.0 + 0.4 * np.random.rand(), np.random.rand(), "grupo1"))

    for i in range(N):
        dataset.append((0.4 + 0.3 * np.random.rand(), 0.2 + 0.5 * np.random.rand(), "grupo2"))

    # mezcla los datos para que no queden las clases separadas
    random.shuffle(dataset)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # recorre datos para clasificarlos y los agrega a la grafica
    for x, y, group in dataset:
        if group == "grupo1":
            # inicializa el grupo con el primer punto
            if g1['x1'] is None:
                g1['x1'] = g1['x2'] = x
                g1['y1'] = g1['y2'] = y
            else:
                if g1['x1'] > x:
                    g1['x1'] = x
                if g1['x2'] < x:
                    g1['x2'] = x
                if g1['y1'] > y:
                    g1['y1'] = y
                if g1['y2'] < y:
                    g1['y2'] = y

            color = "green"
        else:
            if g2['x1'] is None:
                g2['x1'] = g2['x2'] = x
                g2['y1'] = g2['y2'] = y
            else:
                if g2['x1'] > x:
                    g2['x1'] = x
                if g2['x2'] < x:
                    g2['x2'] = x
                if g2['y1'] > y:
                    g2['y1'] = y
                if g2['y2'] < y:
                    g2['y2'] = y
            color = "red"
        ax.scatter(x, y, alpha=0.8, s=30, c=color, edgecolors='none')


    # obtiene soporte de margen
    margin_x = {'x': None, 'y': None, 'value': 1000}
    margin_y = {'x': None, 'y': None, 'value': 1000}

    for x, y, group in dataset:
        if group == "grupo1":
            # calcula el margen de todas las aristas y se queda con la maxima
            if x < g2['x1'] and margin_x['value'] > abs(x - g2['x1']):
                margin_x = {'x': x, 'y': y, 'value': abs(x - g2['x1'])}
            if x > g2['x2'] and margin_x['value'] > abs(x - g2['x2']):
                margin_x = {'x': x, 'y': y, 'value': abs(x - g2['x2'])}

            if y < g2['y1'] and margin_y['value'] > abs(y - g2['y1']):
                margin_y = {'x': x, 'y': y, 'value': abs(y - g2['y1'])}
            if y > g2['y2'] and margin_y['value'] > abs(y - g2['y2']):
                margin_y = {'x': x, 'y': y, 'value': abs(y - g2['y2'])}



    print(margin_x)
    print(margin_y)
    ax.scatter(margin_x['x'], margin_x['y'], alpha=0.8, s=30, c='black')
    ax.scatter(margin_y['x'], margin_y['y'], alpha=0.8, s=30, c='blue')

    # para este ejemplo de datos un clasificador no esta contenido dentro del otro. En caso de que asi sea, se debe
    # chequear cual es el clasificador de menor tamaño y dibujar ese

    # grafica clasificador 1
    # plt.plot([g1['x1'], g1['x2'], g1['x2'], g1['x1'], g1['x1']], [g1['y1'], g1['y1'], g1['y2'], g1['y2'], g1['y1']],
    #          c='black')

    # grafica clasificador 2
    plt.plot([g2['x1'], g2['x2'], g2['x2'], g2['x1'], g2['x1']], [g2['y1'], g2['y1'], g2['y2'], g2['y2'], g2['y1']],
             c='black')

    plt.title("Clasificador rectangular")
    plt.show()


# ejecuta actividades
# act1_a1()
# act1_a2()
act1_b()
