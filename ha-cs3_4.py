# ha-cs3_4.py 'header_only'
# Modified for use with .Net8; csX_X in name is class separation
from sklearn.datasets import make_classification
import numpy as np
import pandas as pd
import string
import os

cfile_name = "ha-cs3_4.csv"
cfile_bare = ""
# ── Output format control ──────────────────────────────────────────────
# Set OUTPUT_MODE to one of:
#   'header_only'       - row 1 header, no index column
#   'index_only'       - row 1 no header,index column
#   'header_and_index'  - row 1 header + index column
#   'data_only'         - no header, no index
OUTPUT_MODE = 'header_only'
# ──────────────────────────────────────────────────────────────────────

# Generate classification data with controlled complexity
X, y = make_classification(
    n_samples=300,
    n_features=20,
    n_classes=3,
    n_informative=15,
    n_redundant=0,
    n_repeated=0,
    n_clusters_per_class=1,
    class_sep=3.0,
    flip_y=0.00,
    random_state=1
)
n_features = 20
feature_names = list(string.ascii_uppercase[:n_features])
df = pd.DataFrame(X, columns=feature_names)

# Apply output format based on OUTPUT_MODE
if OUTPUT_MODE == 'header_only':
    df.to_csv(cfile_name, index=False, header=True)
    # Save true labels separately (for evaluating UI performance later)   
    #np.savetxt(f"{cfile_name}", y, delimiter=',', fmt='%d')
    cfile_bare, extension = os.path.splitext(cfile_name)
    np.savetxt(f"{cfile_bare}_true_labels.csv", y, delimiter=',', fmt='%d')
else:
    raise ValueError(f"Unknown OUTPUT_MODE: '{OUTPUT_MODE}'. Choose 'header_only', 'header_and_index', or 'data_only'.")

cfile_bare, extension = os.path.splitext(cfile_name)
print (f"bare = {cfile_bare}")
print(f"Generated {X.shape[0]} samples with {X.shape[1]} features")
print(f"Data saved to {cfile_bare}.csv")
print(f"True labels saved to {cfile_bare}_true_labels.csv (for validation)")