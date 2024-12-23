@echo off
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -r requirements.txt
python -m playwright install chromium
python main.py --count %1
pause
