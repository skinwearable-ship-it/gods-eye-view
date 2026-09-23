@echo off
setlocal
cd /d "%~dp0\..\.."
where py >nul 2>nul
if %errorlevel%==0 (
  py agent\collect.py
  goto :done
)
where python >nul 2>nul
if %errorlevel%==0 (
  python agent\collect.py
  goto :done
)
echo Python 3 was not found.
exit /b 1
:done
echo Report created in:
echo %cd%
pause
