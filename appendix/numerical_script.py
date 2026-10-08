"""
Numerical script: gamma_max(v) for moving thin‑shell curvature bubble
Task‑①: compute gamma_max(v) curve and v_crit table
Unit: G=hbar=c=1
"""
import numpy as np
import matplotlib.pyplot as plt
import csv

def v_crit_from_chi0(chi0):
    """Analytical critical disintegration velocity"""
    numerator = np.sinh(chi0) - 2.0
    denominator = np.sinh(chi0) + 2.0
    if numerator < 0:
        return 0.0
    return np.sqrt(numerator / denominator)

def gamma_max_approx(chi0, eps, v):
    """
    Effective approximate maximal instability growth rate gamma_max = -Im(omega)
    Simplified linear thin‑shell model (not full GR)
    """
    vc = v_crit_from_chi0(chi0)
    if v <= vc:
        return 0.0
    # above critical velocity: approximate growth rate scaling
    gamma = eps * np.sqrt(v**2 - vc**2)
    return gamma

# Parameter grid
chi0_list = [1.0, 2.0, 3.0, 4.0, 5.0]
eps = 0.05
v_arr = np.linspace(0, 0.99, 200)

plt.figure(figsize=(12,7),dpi=150)
vc_table = []

for chi0 in chi0_list:
    vc = v_crit_from_chi0(chi0)
    vc_table.append([chi0, vc])
    gamma_list = [gamma_max_approx(chi0, eps, vv) for vv in v_arr]
    plt.plot(v_arr, gamma_list, label=f"$\chi_0$={chi0:.1f}")
    plt.axvline(x=vc, linestyle="--", alpha=0.6)

plt.xlabel("$v$ (c=1)")
plt.ylabel("$\\gamma_{max}$")
plt.title("$\\gamma_{max}(v)$ for moving thin‑shell curvature bubble")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("gamma_max_plot.png")
plt.close()

# Output v_crit table to csv
with open("v_crit_table.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["chi0","v_crit"])
    for row in vc_table:
        writer.writerow(row)

print("v_crit table:")
for c,vc in vc_table:
    print(f"chi0={c:.1f} , v_crit={vc:.4f}")

print("\nDone. Output: gamma_max_plot.png , v_crit_table.csv")