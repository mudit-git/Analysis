import numpy as np
import matplotlib.pyplot as plt

def plot_rmsf(file_name, color, label, start_residue, plot_index):
    data = np.loadtxt(file_name, comments=['#', '@'])
    residue = data[:, 0]
    rmsf_values = data[:, 1]

    index_start = np.where(residue == start_residue)[0]
    if len(index_start) == 0:
        index_start = 0
        while index_start < len(residue) and residue[index_start] < start_residue:
            index_start += 1
    else:
        index_start = index_start[0]

    plt.plot(residue[index_start:], rmsf_values[index_start:],
             linestyle='-', linewidth=1, color=color, label=label)

    # Mark the starting residue on the x-axis for the first plotted graph
    if plot_index == 0:
        plt.scatter(start_residue, 0, color='black', s=0, zorder=5)
        plt.text(start_residue, -0.01, str(start_residue), rotation=90, va='top', ha='center', fontsize=8)

n = int(input("Enter the number of plots (up to 100): "))

# Define a contrasting color scheme for a white background
colors = plt.cm.tab10(np.linspace(0, 1, n))

for i in range(n):
    file_name = input(f"Enter the file name for plot {i+1}: ")
    label = f'{file_name}'
    start_residue = int(input(f"Enter the starting residue for plot {i+1}: "))

    plot_rmsf(file_name, colors[i], label, start_residue, i)

plt.title('RMS Fluctuation')
plt.xlabel('Residue')
plt.ylabel('Fluctuation (nm)')
plt.grid(True)
plt.legend(loc='upper left')
plt.ylim(bottom=0)

# Adjust font size of x-axis tick labels
plt.xticks(fontsize=8)

plt.show()
