import numpy as np
import matplotlib.pyplot as plt

def plot_energy(file_name, color, label, start_residue):
    data = np.loadtxt(file_name)
    residue = data[:, 0]
    energy_values = data[:, 1]

    start_index = np.where(residue == start_residue)[0][0]
    residue = residue[start_index:]
    energy_values = energy_values[start_index:]

    plt.plot(residue, energy_values, linestyle='-', linewidth=1.5, color=color, label=label)

    return energy_values

graph_title = input("Enter the title for the graph: ")

file_name = input("Enter the .xvg file name: ")

start_residue = int(input("Enter the starting residue number: "))

energy_values = plot_energy(file_name, '#005A8C', label='Energy', start_residue=start_residue)

plt.title(graph_title)
plt.xlabel('Residue')
plt.ylabel('Energy')
plt.grid(False, axis='y')
plt.axhline(0, color='black', linewidth=0.5)

min_energy = np.min(energy_values) - 1
max_energy = np.max(energy_values) + 1

plt.ylim(bottom=min_energy, top=max_energy)

plt.tight_layout()
plt.show()
