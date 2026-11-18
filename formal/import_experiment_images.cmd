@echo off
setlocal
set "EXPERIMENT_IMAGE_DEST=%~dp0"
powershell.exe -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; try { $folder = $env:EXPERIMENT_IMAGE_DEST; $names = @('inst.png', 'quest.png', 'dist_basic.png', 'dist_adva.png', 'dist_over_all.png', 'dist_different.png', 'procedure.png', '123.png', 'volcano.png'); $missing = @($names | Where-Object { -not (Test-Path -LiteralPath (Join-Path $folder $_) -PathType Leaf) }); if ($missing.Count -gt 0) { throw ('Put these image files beside the experiment files: ' + ($missing -join ', ')) }; Write-Host 'All 9 image files are beside the experiment. Open distribution_reconstruction.psyexp in PsychoPy and run it.'; exit 0 } catch { Write-Host ('Image check failed: ' + $_.Exception.Message); exit 1 } }"
if errorlevel 1 (
    echo.
    echo Required image files are missing. See the error above.
    pause
    exit /b 1
)
echo.
pause
