echo off

cd ..
pyinstaller --onefile --icon "compile to exe/icon.ico" --distpath "compile to exe/" "app.py"

del /s /q /f app.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null