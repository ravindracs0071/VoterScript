@echo off
echo 'Script Starting Execution ...'
:loop
set ldt=%date% %time%
echo %ldt%
"C:\Users\ravindra\AppData\Local\Programs\Python\Python38\python.exe" VoteApp.py
choice /T 1830 /D N /N
goto loop
REM pause
echo 'Script End Execution ...'

exit 0