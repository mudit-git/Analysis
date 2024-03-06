import numpy as np
import matplotlib.pyplot as plt

def plot_hbonds(file_name, color, label, column):
    data = np.loadtxt(file_name, comments=['#', '@'])
    time = data[:, 0]
    hbond_values = data[:, column]

    plt.bar(time, hbond_values, color=color, label=label, alpha=0.7)

def plot_hbonds_stats(time, max_values, min_values, median_values, label):
    plt.figure()
    plt.bar(time, max_values, color='red', label=f'Maximum {label}', alpha=0.7)
    plt.bar(time, min_values, color='blue', label=f'Minimum {label}', alpha=0.7)
    plt.bar(time, median_values, color='green', label=f'Median {label}', alpha=0.7)

    plt.title(f'{label} Statistics')
    plt.xlabel('Time (ns)')
    plt.ylabel('Number')
    plt.grid(True)
    plt.legend()

n = int(input("Enter the number of plots (n): "))

file_names = []
colors = []
labels = []

max_values_hbonds = np.zeros(0)
min_values_hbonds = np.zeros(0)
median_values_hbonds = np.zeros(0)

for i in range(n):
    file_name = input(f"Enter the file name for plot {i+1}: ")
    color = plt.cm.viridis(i / n)
    label = f'{file_name}'

    file_names.append(file_name)
    colors.append(color)
    labels.append(label)

    data = np.loadtxt(file_name, comments=['#', '@'])
    time = data[:, 0]
    hbond_values = data[:, 1]

    if i == 0:
        max_values_hbonds = hbond_values
        min_values_hbonds = hbond_values
        median_values_hbonds = hbond_values
    else:
        max_values_hbonds = np.maximum(max_values_hbonds, hbond_values)
        min_values_hbonds = np.minimum(min_values_hbonds, hbond_values)
        median_values_hbonds += hbond_values

    plot_hbonds(file_name, color, label + ' - Hydrogen bonds', column=1)

median_values_hbonds /= n

plot_hbonds_stats(time, max_values_hbonds, min_values_hbonds, median_values_hbonds, label='Hydrogen Bonds')

plt.show()
