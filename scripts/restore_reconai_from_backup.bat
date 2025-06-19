@echo off
echo Restoring Recon.AI project from My Book (H:) to D: drive ...
robocopy "H:\ReconAI\backups\latest" "D:\ReconAI\reconai-site" /MIR /Z /R:2 /W:2
echo Restore complete.
pause
