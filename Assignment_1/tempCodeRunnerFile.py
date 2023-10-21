import matplotlib.pyplot as plt

def show_graph(data):
    x = list(range(len(data)))
    y = data
    plt.plot(x, y)
    plt.show()
data = list_n
show_graph(data)