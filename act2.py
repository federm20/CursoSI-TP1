import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv',
    delimiter=",")

print(data)

color = {
    'Virginica': 'green',
    'Versicolor': 'red',
    'Setosa': 'blue'
}

for x in data.iterrows():
    if x[1]['variety'] == 'Setosa':
        continue
    plt.plot(x[1]['petal.length'], x[1]['petal.width'], marker='o', c=color[x[1]['variety']])

plt.title("Pétalos de Iris (largo x ancho)")
plt.show()
