# SeedClustering — Installation & Getting Started Guide

## Overview

SeedClustering is a demonstration application for clustering dataset analysis of unsupervised training and inference.
It comes pre-loaded with example CSV data files so you can explore its features immediately.
When you are ready, simply replace the example raw dataset, true labels, and sanitized dataset CSV files with your own datasets.

---

## System Requirements

- A Windows PC with a **C: drive**
- Approximately 154 MB free disk space to hold the unzipped contents of `SeedClustering.zip`
- No additional software installation is required — Python is embedded within the application

---

## Downloading SeedClustering

There are two ways to obtain SeedClustering. Choose whichever suits you best.

---

### Option 1 — Download via ZIP file (simplest, no Git required)

If you have been sent a `SeedClustering.zip` file directly (e.g. via a Google Drive link):

1. Click the shared Google Drive link provided to you.
2. If Google displays a warning saying *"Google Drive can't scan this file for viruses"*, click **Download anyway** — this is a standard Google notice for large files and is not an indication of any problem with the file.
3. Save `SeedClustering.zip` to a convenient location (e.g. your `Downloads` folder).
4. Create an empty directory on your C: drive:
   ```
   C:\SC
   ```
5. Move `SeedClustering.zip` into `C:\SC`.
6. Right-click `SeedClustering.zip` and select **Extract Here** (or use your preferred zip utility).

> **Important:** Extract directly into `C:\SC` so all files land at the `C:\SC\` root level. Do not extract into a subfolder.

---

### Option 2 — Download from GitHub

The SeedClustering project is also hosted at **github.com/jimbr99/SeedClustering**. To download it:

1. Open your browser and navigate to:
   ```
   https://github.com/jimbr99/SeedClustering
   ```
2. Click the green **"Code"** button near the top right of the page.
3. Select **"Download ZIP"** from the dropdown menu. This downloads a file named `SeedClustering-main.zip`.
4. Locate `SeedClustering-main.zip` (typically in your `Downloads` folder) and unzip it.
5. Inside the unzipped folder you will find a subfolder named `SeedClustering-main\` containing all application files.
6. Create an empty `C:\SC` directory and **move all contents** of `SeedClustering-main\` into it.

> **Important:** Do not simply unzip into `C:\SC` directly — Windows will create `C:\SC\SeedClustering-main\` as a subdirectory, and the application will not run correctly from that path. All files must be at the `C:\SC\` root level.

---

## Expected Directory Contents

After extraction by either method, your `C:\SC` directory should contain at minimum:

```
C:\SC\
├── SeedClustering.exe        ← Main application executable
├── python_path               ← File used to locate embedded Python
├── python_env\               ← Embedded Python environment (do not modify)
│   └── (Python 3.11 runtime files)
├── CPython311python.exe.bat  ← Utility to reinstall embedded Python if needed
├── input_files.txt           ← List of four *.csv files, with raw file first in list
├── clustering_model.zip      ← Zipped model file. Do not unzip — application uses it as-is
└── *.csv                     ← Example seed dataset files
```

> **Important:** All files must remain in `C:\SC`. The application expects to find its resources, dataset files, and embedded Python at this specific location.

---

## Running SeedClustering.exe

Once the files are extracted:

1. Open **File Explorer** and navigate to `C:\SC`.
2. **Double-click** `SeedClustering.exe` to launch the application.
3. Or, use CLI to navigate to `C:\SC` and enter `SeedClustering.exe` and hit return to run.
4. The application opens and runs in a CLI window.

No further configuration is needed.

---

## Using Your Own Data

SeedClustering ships with example `*.csv` files to demonstrate its features. To analyze your own datasets:

1. Review the format of the included example `*.csv` files to understand the expected 20-column structure.
2. Replace the example `*.csv` files in `C:\SC` with your own CSV files, following the same format.
3. Update `input_files.txt` with your own dataset filenames, placing the raw dataset filename first in the list.
4. Launch `SeedClustering.exe` to run the application.

---

## Embedded Python

SeedClustering includes an embedded **Python 3.11** runtime located in the `python_env` subdirectory.
You do **not** need to install Python separately. The file `python_path` tells the application where to find this runtime.

**Do not move or rename the `python_env` directory**, as this will prevent the application from functioning correctly.

### Reinstalling Embedded Python (if needed)

In the unlikely event that the embedded Python environment becomes corrupted, a reinstallation batch file is included:

```
C:\SC\CPython311python.exe.bat
```

Double-click this file to reinstall the embedded Python environment. This should rarely, if ever, be necessary.

---

## Troubleshooting

| Problem | Suggested Action |
|---|---|
| Application does not launch | Verify all files were extracted to `C:\SC` and that `SeedClustering.exe` is present |
| Python-related error on startup | Run `CPython311python.exe.bat` to reinstall the embedded Python environment |
| CSV data not loading | Ensure your CSV files are in `C:\SC` and match the expected format of the example files |
| Google Drive warning on ZIP download | Click **"Download anyway"** — this is normal for large files and not a security issue |

---

## Summary of Key Files

| File / Directory | Purpose |
|---|---|
| `SeedClustering.exe` | Main application — double-click to run in Windows, or use CLI |
| `python_env\` | Embedded Python 3.11 runtime (do not modify) |
| `python_path` | Tells the application where to find embedded Python |
| `CPython311python.exe.bat` | Reinstalls embedded Python if needed |
| `*.csv` | Example seed dataset files (replace with your own) |
| `input_files.txt` | Populates file selection during application run |
| `clustering_model.zip` | Zipped model file — do not unzip, used directly by the application |
