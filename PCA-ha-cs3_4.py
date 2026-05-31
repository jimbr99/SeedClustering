# PCA-ha-cs3_4.py
# Usage:
#   Raw file:        python PCA-ha-cs3_4.py ha-cs3_4.csv 42 raw
#   Normalized file: python PCA-ha-cs3_4.py ha-cs3_4_xxxxx.csv 42 prescaled
#
# Arguments:
#   sys.argv[1] : input CSV file name
#   sys.argv[2] : seed number (reserved for future use)
#   sys.argv[3] : "raw" (default) or "prescaled"
#                 raw       = script applies StandardScaler internally
#                 prescaled = data is already conditioned, skip scaling

import os
import sys
import threading
import numpy as np
import matplotlib
matplotlib.use('Agg') # force interactive backend
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pathlib import Path
import pandas as pd

# ── Command line arguments ────────────────────────────────────────────────────
var1     = sys.argv[1]                                    # input CSV file
var2     = sys.argv[2]                                    # seed (reserved)
var3     = sys.argv[3] # if len(sys.argv) > 3 else "raw"   # raw | prescaled
bestSeed = var2
'''
def wait_for_cs_signal():
    # Wait for the newline sent by process.StandardInput.WriteLine() in C#
    sys.stdin.readline()
    print("Closing plot server...")
    # This triggers the exit of the plt.show() loop
    plt.close('all')
# Start the listener thread
threading.Thread(target=wait_for_cs_signal, daemon=True).start()
'''
# ── Paths ─────────────────────────────────────────────────────────────────────
path = os.path.abspath(__file__)
print(f"Script path : {path}")
cwd = os.getcwd()
print(f"CWD         : {cwd}")

dataset_name = var1
print(f"Input file  : {dataset_name}")
print(f"Mode        : {var3}")

# ── Locate input file ─────────────────────────────────────────────────────────
def access_remote_file():
    base_dir    = Path(__file__).resolve().parent
    target_file = base_dir / dataset_name
    print(f"Base dir    : {base_dir}")
    print(f"Target file : {target_file}")
    return target_file

dataset_target = access_remote_file()
print(f"Remote file : {dataset_target}")

# ── Load CSV (replace text headers with numeric indices) ──────────────────────
"""
df = pd.read_csv(dataset_target, header=0)
df.columns = range(df.shape[1])
print(f"Columns     : {list(df.columns)}")
df.to_csv('temp_dataset.csv', index=False)
X = np.loadtxt("temp_dataset.csv", delimiter=',')
print(f"Data shape  : {X.shape}")
"""
df = pd.read_csv(dataset_target, header=0)
df.columns = range(df.shape[1])

# Convert directly to numpy array — no temp file needed
# This avoids np.loadtxt reading the header row as data
X = df.values.astype(float)
print(f"Data shape  : {X.shape}")

# ── Scale only if raw data; skip if already conditioned ───────────────────────
if var3 == "raw":
    print("Scaling     : StandardScaler applied (raw mode)")
    X_for_pca = StandardScaler().fit_transform(X)
else:
    print("Scaling     : skipped (prescaled mode)")
    X_for_pca = X

# ── PCA projection to 2D ──────────────────────────────────────────────────────
pca  = PCA(n_components=2)
X_2d = pca.fit_transform(X_for_pca)

pc1_var = pca.explained_variance_ratio_[0]
pc2_var = pca.explained_variance_ratio_[1]
print(f"PC1 variance: {pc1_var:.1%}")
print(f"PC2 variance: {pc2_var:.1%}")

# ── KMeans clustering (same data as PCA for consistency) ──────────────────────
print(f"KMeans seed : {bestSeed}")
kmeans           = KMeans(n_clusters=3, random_state= int(bestSeed)) # 5
print(f"KMeans done")
predicted_labels = kmeans.fit_predict(X_for_pca)
print(f"predicted_labels done")
unique, counts = np.unique(predicted_labels, return_counts=True)
print("Cluster counts:")
for u, c in zip(unique, counts):
    print(f"  Cluster {u}: {c} rows")

# ── Plot ──────────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    X_2d[:, 0], X_2d[:, 1],
    c=predicted_labels,
    cmap='viridis',
    alpha=0.6,
    edgecolors='k'
)
plt.colorbar(scatter, label='Cluster')
plt.xlabel(f'PC1 ({pc1_var:.1%} variance)')
plt.ylabel(f'PC2 ({pc2_var:.1%} variance)')


if var3 == "raw":
    mode_label = "raw"
elif var3 == "prescaled":
    mode_label = "prescaled"
else: mode_label = "prescaledMax"
print(f"mode_label: {mode_label}")
#if var3 == "raw" else "prescaled"
plt.title(
    f'processed dataset "{dataset_name}" Clustering Results '
    f'(PCA Projection) [{mode_label}]'
)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# ── Save plot ─────────────────────────────────────────────────────────────────
import subprocess

outpng = dataset_name[:-4] + f"_{mode_label}.png"
plt.savefig(outpng, dpi=300)
print(f"Plot saved  : {outpng}")
#print(f"PRESS ANY KEY IN THIS CONSOLE TO CLOSE PLOT.")
#plt.show()
#png_full_path = os.path.join(base_dir, plot_save_path)   
cwd = os.getcwd()
png_full_path = os.path.join(cwd, outpng)
# 1. Open the image using the default Windows viewer
os.startfile(png_full_path)

print("Plot generated. Send a keypress/newline on Console to close viewer.", flush=True)

# 2. Wait for C# to send a keypress/newline via Standard Input
sys.stdin.readline()


'''
if os.path.exists(png_full_path):
    print(f"Python: Opening plot: {png_full_path}")
    #subprocess.Popen(['cmd', '/c', 'start', '', png_full_path], shell=False)
    ["cmd", "/c", png_full_path], shell=False, creationflags=subprocess.CREATE_NO_WINDOW
else:
    print(f"Python: WARNING - PNG not found at {png_full_path}")
print(f"png_full_path: {png_full_path}")
print(f"PRESS ANY KEY IN THIS CONSOLE TO CLOSE PLOT.")
sys.stdin.read(1)
'''

subprocess.run(
    #["taskkill", "/F", "/T", "/FI", f"IMAGE_PATH eq {png_full_path}"],
    f'taskkill /F /FI "WINDOWTITLE eq {os.path.basename(png_full_path)}*"',
    shell=True,
	stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
print(f"Finished Plot...")

sys.exit(0)

