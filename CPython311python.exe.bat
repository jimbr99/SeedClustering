@echo off
SETLOCAL EnableDelayedExpansion

:: ---------------------------------------------------------------
:: Configuration
:: ---------------------------------------------------------------
set "TARGET_DIR=C:\SC\python_env"
set "PY_VER=3.11.9"
set "PY_ZIP=python-%PY_VER%-embed-amd64.zip"
set "PY_URL=https://www.python.org/ftp/python/%PY_VER%/%PY_ZIP%"
set "PIP_URL=https://bootstrap.pypa.io/get-pip.py"
set "PTP_FILE=python311._pth"

echo ===================================================
echo  Embedded Python Installer for SeedClustering
echo  Target: %TARGET_DIR%
echo ===================================================
echo.

:: ---------------------------------------------------------------
:: Step 1: Create target directory
:: ---------------------------------------------------------------
echo [1/5] Creating directory...
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"
if errorlevel 1 (
    echo ERROR: Could not create directory %TARGET_DIR%
    pause
    exit /b 1
)
cd /d "%TARGET_DIR%"
echo       Done. OK
echo.

:: ---------------------------------------------------------------
:: Step 2: Download and extract embeddable Python
:: ---------------------------------------------------------------
echo [2/5] Downloading Python %PY_VER% embeddable package...
curl -L -o "%PY_ZIP%" "%PY_URL%"
if errorlevel 1 (
    echo ERROR: Download failed. Check internet connection.
    echo URL attempted: %PY_URL%
    pause
    exit /b 1
)
echo       Download complete. Extracting...
powershell -Command "Expand-Archive -Path '%PY_ZIP%' -DestinationPath '.' -Force"
if errorlevel 1 (
    echo ERROR: Extraction failed.
    pause
    exit /b 1
)
del "%PY_ZIP%"
echo       Extraction complete. OK
echo.

:: ---------------------------------------------------------------
:: Step 3: Enable site-packages in the .pth file
:: This is critical — without it pip-installed packages
:: will not be found by the embedded Python interpreter
:: ---------------------------------------------------------------
echo [3/5] Enabling site-packages...
if not exist "%PTP_FILE%" (
    echo ERROR: %PTP_FILE% not found in %TARGET_DIR%
    echo        Extraction may have failed or file name differs.
    dir *.pth
    pause
    exit /b 1
)

:: Uncomment the "import site" line by removing the leading #
powershell -Command ^
    "(Get-Content '%PTP_FILE%') -replace '^#import site', 'import site' | Set-Content '%PTP_FILE%'"

echo       Site-packages enabled. OK
echo.

:: ---------------------------------------------------------------
:: Step 4: Download and install pip
:: ---------------------------------------------------------------
echo [4/5] Installing pip...
curl -L -o get-pip.py "%PIP_URL%"
if errorlevel 1 (
    echo ERROR: Could not download get-pip.py
    echo URL attempted: %PIP_URL%
    pause
    exit /b 1
)
.\python.exe get-pip.py --no-warn-script-location
if errorlevel 1 (
    echo ERROR: pip installation failed.
    pause
    exit /b 1
)
del get-pip.py
echo       pip installed. OK
echo.

:: ---------------------------------------------------------------
:: Step 5: Install required Python libraries
:: ---------------------------------------------------------------
echo [5/5] Installing required libraries...
echo       This may take several minutes...
echo.
.\python.exe -m pip install ^
    "numpy>=1.26.0,<2.0" ^
    "pandas>=2.1.0" ^
    "scikit-learn" ^
    "matplotlib"

if errorlevel 1 (
    echo ERROR: Library installation failed.
    echo        Check the error messages above.
    pause
    exit /b 1
)


echo ===================================================
echo  INSTALLATION COMPLETE
echo.
echo  Python executable location:
echo  %TARGET_DIR%\python.exe
echo.
echo  Add this path to python_path.txt:
echo  %TARGET_DIR%\python.exe
echo ===================================================
pause

echo.
echo ===================================================
echo  INSTALLATION COMPLETE
echo.
echo  Python executable location:
echo  %TARGET_DIR%\python.exe
echo.
echo  Add this path to python_path.txt:
echo  %TARGET_DIR%\python.exe
echo ===================================================
pause