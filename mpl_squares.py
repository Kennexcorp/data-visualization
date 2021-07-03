import matplotlib.pyplot as plt

"""A simple line graph"""

class LineGraph:

    def __init__(self):
        self.squares = [1, 4, 9, 16, 25, 36, 49]
        self.input_values = [1, 2, 3, 4, 5, 6, 7]
        self.linewidth = 3
        self.title = "Square Numbers"
        self.fontsize = 12

    def plot_line_graph(self):
        plt.style.use('Solarize_Light2')
        fig, ax = plt.subplots()
        ax.plot(self.input_values, self.squares, self.linewidth)

        ax.set_title(self.title, fontsize=self.fontsize)
        ax.set_xlabel("Value", fontsize=self.fontsize)
        ax.set_ylabel("Square of value", fontsize=self.fontsize)

        ax.tick_params(axis='both', labelsize=self.fontsize)

        plt.show()

line_graph = LineGraph()
line_graph.plot_line_graph()