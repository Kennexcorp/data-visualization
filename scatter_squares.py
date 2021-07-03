import matplotlib.pyplot as plt

"""A scatter squares graph"""

class ScatterSquares:

    def __init__(self):
        self.x_values = range(1, 10001)
        self.y_values = [x**2 for x in self.x_values]
        self.linewidth = 3
        self.title = "Square Numbers"
        self.fontsize = 12

    def plot_scatter_squares(self):
        plt.style.use('Solarize_Light2')
        fig, ax = plt.subplots()
        ax.scatter(self.x_values, self.y_values, cmap=plt.cm.Blues, s=10)

        ax.set_title(self.title, fontsize=self.fontsize)
        ax.set_xlabel("Value", fontsize=self.fontsize)
        ax.set_ylabel("Square of value", fontsize=self.fontsize)

        ax.tick_params(axis='both', which='major', labelsize=self.fontsize)
        ax.axis([0, 1100, 0, 1100000])
        plt.show()

scatter_squares = ScatterSquares()
scatter_squares.plot_scatter_squares()