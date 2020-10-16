call project_env\Scripts\activate.bat
call pyinstaller server.py -y
call xcopy templates dist\server\templates\ /E /y
call xcopy config.xlsx dist\server\config.xlsx /y