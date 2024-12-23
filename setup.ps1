# Запустить от имени администратора
Set-ExecutionPolicy Bypass -Scope Process -Force
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup completed! Now you can run: python main.py"
pause
