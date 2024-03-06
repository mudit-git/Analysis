import numpy as np
import matplotlib.pyplot as plt


def plot_rmsd(file_name, color, label):
    data = np.loadtxt(file_name, comments=['#', '@'])
    time = data[:, 0]
    rmsd_values = data[:, 1]

    plt.plot(time, rmsd_values, linestyle='-', linewidth=0.75, color=color, label=label)


n = 2
colors = ['black', 'red']

graph_title = input("Enter the title for the graph: ")

for i in range(n):
    file_name = input(f"Enter the file name for plot {i + 1}: ")
    label = f'{file_name}'

    plot_rmsd(file_name, colors[i], label)

plt.title(graph_title)
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (nm)')
plt.grid(False)

plt.tight_layout()
plt.show()
