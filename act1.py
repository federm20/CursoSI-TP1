import numpy as np
import matplotlib.pyplot as plt

def act1_a1():
    plt.plot(3.5, 5, 5, 8, 6.5, 5, marker='o', c='red')
    plt.plot(4.5, 3, 4, 7, 5.5, 3, 6, 7, marker='o', c='green')
    plt.plot([3.3, 6.7, 5, 3.3], [4.8, 4.8, 8.2, 4.8], c='black')
    plt.title("Dimensión VC Triángulo")
    plt.legend(loc=2)
    plt.show()

# def act1_a2():
#     plt.plot(3.5, 5, 5, 8, 6.5, 5, marker='o', c='red')
#     plt.plot(4.5, 3, 4, 7, 5.5, 3, 6, 7, marker='o', c='green')
#     plt.plot([3.3, 6.7, 5, 3.3], [4.8, 4.8, 8.2, 4.8], c='black')
#     plt.title("Dimensión VC Hiperplano")
#     plt.legend(loc=2)
#     plt.show()

act1_a1()

def act1_b():
    # Create data
    N = 60
    g1 = (0.0 + 0.4 * np.random.rand(N), np.random.rand(N))
    g2 = (0.4 + 0.3 * np.random.rand(N), 0.2 + 0.5 * np.random.rand(N))

    dataset = []

    for i in range(N):
        dataset.append((0.0 + 0.4 * np.random.rand(), np.random.rand(), "grupo1"))

    for i in range(N):
        dataset.append((0.4 + 0.3 * np.random.rand(), 0.2 + 0.5 * np.random.rand(), "grupo2"))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for x, y, group in dataset:
        if group == "grupo1":
            color = "green"
        else:
            color = "red"
        ax.scatter(x, y, alpha=0.8, s=30, c=color, edgecolors='none')

    plt.title("Data")
    plt.legend(loc=2)
    plt.show()


#
#
# dataset = (g1, g2)
# colors = ("red", "green")
# groups = ("coffee", "tea")
#
# # Create plot
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# def print_data():
#     for data, color, group in zip(dataset, colors, groups):
#         x, y = data
#         ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
#
#     plt.title('Data')
#     plt.legend(loc=2)
#     plt.show()
#
#
# # print_data()
#
# for data, color, group in zip(dataset, colors, groups):
#     x, y = data
#     ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
#
# plt.title('Data')
# plt.legend(loc=2)
# plt.show()


