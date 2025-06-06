import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
plt.style.use('bmh')
plt.rcParams['figure.figsize'] = 8, 5
#plt.rcParams['figure.labelsize'] = 15
rcParams["figure.subplot.hspace"] = (0.2)

def load_data(file_path):
    """Load seismic data from file."""
    data = np.loadtxt(file_path)
    time = data[:, 0]
    magnitude = data[:, 1]
    return time, magnitude

def plot_time_series(time, magnitude):
    """Plot magnitude over time."""
    plt.figure(figsize=(12, 5))
    plt.plot(time, magnitude, '.', markersize=2, color='green')
    plt.xlabel("Time (days)")
    plt.ylabel("Magnitude")
    plt.title("Microseismic Magnitude vs Time")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../figures/Microseismic Magnitude vs Time", dpi=300)
    plt.show()

if __name__ == "__main__":
    time, magnitude = load_data("../data/M_data1.txt")
    plot_time_series(time, magnitude)