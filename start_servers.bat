@echo off
REM Set PYTHONPATH to the 'chatproject' folder so Python can find the modules correctly
set PYTHONPATH=%CD%\chatproject

REM Activate the virtual environment
call venv\Scripts\activate.bat
echo ==============================================
echo   Starting Daphne server on http://0.0.0.0:8000 ...
echo ==============================================

REM Change directory to 'chatproject', where manage.py and asgi.py live
cd chatproject

REM Run Daphne binding to all IP addresses on port 8000 with the ASGI application
daphne -b 0.0.0.0 -p 8000 chatproject.asgi:application
