For task 3 there was created a virtual environment.  
If cloned this repo, there is no such folder as .venv (because it's ignored by git configs), so you need to create it using next command in cmd or powershell  
(I tried terminal in VS Code, but it didn't work):

```cmd
python -m venv .venv
```

If you already have this folder, next you need to activate a virtual environment by running next command:

For cmd:
```cmd
.\.venv\Scripts\activate.bat
```

For powershell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Then you might need to install required packages:

```cmd
pip install -r requirements.txt
```

Then run the script for task #3:

```cmd
python tasks/task_3.file_explorer.py D:\Python\goit-pycore-hw-04
```

To deactivate a virtual environment:

```cmd
deactivate
```
