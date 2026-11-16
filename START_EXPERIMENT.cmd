@echo off
setlocal
set "EXPERIMENT_DIR=%~dp0"
set "DESKTOP_DIR=%USERPROFILE%\Desktop"
set "PSYCHOPY_PYTHON="

if exist "%DESKTOP_DIR%\PsychoPy\python.exe" set "PSYCHOPY_PYTHON=%DESKTOP_DIR%\PsychoPy\python.exe"

if not defined PSYCHOPY_PYTHON (
    for /d %%D in ("%DESKTOP_DIR%\*") do (
        if exist "%%~fD\PsychoPy\python.exe" set "PSYCHOPY_PYTHON=%%~fD\PsychoPy\python.exe"
    )
)

if not defined PSYCHOPY_PYTHON (
    echo Could not find PsychoPy's python.exe on the Desktop.
    echo Open this file in a text editor and check the PsychoPy installation path.
    echo.
    pause
    exit /b 1
)

echo Starting experiment with:
echo "%PSYCHOPY_PYTHON%"
echo.
pushd "%EXPERIMENT_DIR%"
"%PSYCHOPY_PYTHON%" -u "%EXPERIMENT_DIR%distribution_reconstruction_run.py"
set "RUN_RESULT=%ERRORLEVEL%"
popd

if not "%RUN_RESULT%"=="0" (
    echo.
    echo The experiment stopped with exit code %RUN_RESULT%.
) else (
    echo.
    echo The experiment closed normally.
)
echo.
pause
exit /b %RUN_RESULT%
