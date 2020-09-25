@ECHO OFF
TITLE Link Budget Tool CLI
mode 100,60
ECHO ===================================================================================================
ECHO Installing dependencies...
pip3 --version
pip3 install numpy
ECHO ===================================================================================================
ECHO.
ECHO Ready to start!
ECHO.
python main.py
