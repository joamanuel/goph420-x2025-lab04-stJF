import sys
import os
sys.path.append(os.path.abspath("../src"))
import numpy as np
import matplotlib.pyplot as plt
from lab_04.regression import multi_regress

def load_data(file_path):
    data = np.loadtxt(file_path)
    return data[:, 0], data[:, 1]

def filter_by_time(time, magnitude, tmin, tmax):
    mask = (time >= tmin) & (time <= tmax)
    return magnitude[mask]

def compute_M_N(magnitudes, bin_width=0.1):
    M_bins = np.arange(np.min(magnitudes), np.max(magnitudes) + bin_width, bin_width)
    hist, bin_edges = np.histogram(magnitudes, bins=M_bins)
    N = np.cumsum(hist[::-1])[::-1]
    M_plot = bin_edges[:-1]
    mask = N > 0
    return M_plot[mask], N[mask]

def fit_and_plot(ax, M, N, title):
    logN = np.log10(N)
    Z = M.reshape(-1, 1)
    a_vec, e, r2 = multi_regress(logN, Z)
    a0, b = a_vec
    logN_pred = a0 + b * M

    ax.plot(M, logN, 'o', markersize=4, label='Data')
    ax.plot(M, logN_pred, 'r-', label=f'Fit: log₁₀N = {a0:.2f} {b:+.2f}M\nR² = {r2:.3f}')
    ax.set_title(title)
    ax.set_xlabel("Magnitude (M)")
    ax.set_ylabel("log₁₀(N ≥ M)")
    ax.grid(True)
    ax.legend()

    print(f"[{title}] Estimated a = {a0:.4f}, b = {-b:.4f}, R² = {r2:.4f}")

def main():
    time, magnitude = load_data("../data/M_data1.txt")

    # Define time windows
    intervals = [
        (0, 5, "Period A: 0–25 days"),
        (20, 80, "Period B: 40–60 days"),
        (115, 120, "Period C: 100–120 days")
    ]

    fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)

    for ax, (tmin, tmax, title) in zip(axes, intervals):
        mags_filtered = filter_by_time(time, magnitude, tmin, tmax)
        M, N = compute_M_N(mags_filtered)
        fit_and_plot(ax, M, N, title)

    fig.suptitle("Gutenberg-Richter Regression for Three Time Periods", fontsize=14)
    plt.tight_layout()
    plt.savefig("../figures/sample_plot.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
