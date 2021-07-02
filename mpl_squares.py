import matplotlib.pyplot as plt

"""A simple line graph"""

class LineGraph:

    def __init__(self):
        self.squares = [1, 4, 9, 16, 25]

    def plot_line_graph(self):
        fig, ax = plt.subplots()
        ax.plot(self.squares)

        plt.show()

line_graph = LineGraph()
line_graph.plot_line_graph()