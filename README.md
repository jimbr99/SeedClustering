SeedClustering — Installation & Getting Started Guide
Overview
SeedClustering is a demonstration application for clustering dataset analysis of unsupervised training and inference.
It comes pre-loaded with example CSV data files so you can explore its features immediately.
When you are ready, simply replace the example raw dataset, true labels, and sanitized dataset CSV files with your own datasets.
---
System Requirements
A Windows PC with a C: drive
Approximately 154 MB free disk space to hold the unzipped contents of `SeedClustering.zip`
No additional software installation is required — Python is embedded within the application
---
Downloading from GitHub
The SeedClustering project is hosted at github.com/jimbr99/SeedClustering. To download it:
Open your browser and navigate to the repository:
```
   https://github.com/jimbr99/SeedClustering
   ```
Click the green "Code" button near the top right of the page.
Select "Download ZIP" from the dropdown menu. This downloads a file named `SeedClustering-main.zip`.
Locate the downloaded `SeedClustering-main.zip` file (typically in your `Downloads` folder) and unzip it.
Inside the unzipped folder you will find a subfolder named `SeedClustering-main\` containing all application files.
Move all contents of `SeedClustering-main\` into a new empty `C:\SC` directory on your C: drive.
> **Important:** Do not simply unzip into `C:\SC` directly — Windows will create `C:\SC\SeedClustering-main\` as a subdirectory, and the application will not run correctly from that path. All files must be at the `C:\SC\` root level.
---
Installation
Create an empty directory at the following path on your C: drive:
```
   C:\SC
   ```
Follow the Downloading from GitHub steps above to download and unzip the repository.
Move all contents from the unzipped `SeedClustering-main\` folder into `C:\SC`.  
After extraction, your directory should contain at minimum:
```
   C:\SC\
   ├── SeedClustering.exe        ← Main application executable
   ├── python_path               ← File used to locate embedded Python
   ├── python_env\               ← Embedded Python environment (do not modify)
   │   └── (Python 3.11 runtime files)
   ├── CPython311python.exe.bat  ← Utility to reinstall embedded Python if needed
   └── *.csv                     ← Example seed dataset files
   └── input_files.txt			 ← list of four *.csv files, with raw file first in list
   └── clustering_model.zip		 ← Zipped model file. Do not unzip as application uses it
   └── various other support files
   ``` 
> **Important:** All files must remain in `C:\SC`. The application expects to find its resources, 
dataset files, and embedded Python at this specific location.
---
Running SeedClustering.exe
Once the files are extracted:
Open File Explorer and navigate to `C:\SC`.
Double-click `SeedClustering.exe` to launch the application.
Or, use CLI to navigate to `C:\SC` and enter SeedClustering.exe and hit return to run.
The appliction opens and runs in a CLI window.
No further configuration is needed.
---
Using Your Own Data
SeedClustering ships with example `*.csv` files to demonstrate its features. To analyze your own datasets:
Review the format of the included example `*.csv` files to understand the expected (20)column structure.
Replace the example `*.csv` files in `C:\SC` with your own CSV files, following the same format.
Update the file input_files.txt with your own sanitized datasets, using the raw dataset first in the list.
Launch `SeedClustering.exe` to run application.
---
Embedded Python
SeedClustering includes an embedded Python 3.11 runtime located in the `python_env` subdirectory.
You do not need to install Python separately. The file `python_path` tells the application where to find this runtime.
Do not move or rename the `python_env` directory, as this will prevent the application from functioning correctly.
Reinstalling Embedded Python (if needed)
In the unlikely event that the embedded Python environment becomes corrupted, a reinstallation batch file is included:
```
C:\SC\CPython311python.exe.bat
```
Double-click this file to reinstall the embedded Python environment. This should rarely, if ever, be necessary.
---
Troubleshooting
Problem	Suggested Action
Application does not launch	Verify all files were extracted to `C:\SC` and that `SeedClustering.exe` is present
Python-related error on startup	Run `CPython311python.exe.bat` to reinstall the embedded Python environment
CSV data not loading	Ensure your CSV files are in `C:\SC` and match the expected format of the example files
---
Summary of Key Files
File / Directory	Purpose
`SeedClustering.exe`	Main application — double-click to run in Windows, or use CLI to run
`python_env\`	Embedded Python 3.11 runtime (do not modify)
`python_path`	Tells the application where to find embedded Python
`CPython311python.exe.bat`	Reinstalls embedded Python if needed
`*.csv`	Example seed data files (replace with your own)
`input_files`	populates pop-up file selection during application run
