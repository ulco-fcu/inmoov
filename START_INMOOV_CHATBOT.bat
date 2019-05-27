REG ADD HKCU\Console /v CodePage /t REG_DWORD /d 0xfde9 /f
REG ADD HKCU\Console /v FaceName /t REG_SZ /d "Lucida Console" /f
@chcp 65001>nul
@echo off
echo ------------------------------------------------------
echo 			INMOOV BATCH LAUNCHER 0.2
echo    LAUNCHER PERMETTANT DE LANCER UNIQUEMENT
echo    LE CHATBOT
echo ------------------------------------------------------
echo .
echo KILL JAVA to clean reborn
taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
echo ------------------------------------------------------
echo LOG CLEAN UP to free space disk and send clean noworky
echo ------------------------------------------------------
del myrobotlab.log > NUL
echo .

cls
echo ------------------------------------------------------
echo DEMARRAGE MRL ET SERVICE chatbot : PROGRAM-AB
echo ------------------------------------------------------
if not exist %cd%\Inmoov\InMoov-chatbot.py (
COLOR 4F
echo ERROR : %cd%\InMoov\InMoov-chatbot.py is not available
echo CHECK ABOUT SPACES INSIDE FOLDERS NAME or SPECIAL CHARACTERS 
echo "c:\mrl" is a great place to start
timeout 10 > NUL
) else (java -Dfile.encoding=UTF-8 -jar myrobotlab.jar -jvmargs="-Dfile.encoding=UTF-8" -invoke python execFile %cd%/InMoov/InMoov-chatbot.py -service python Python)
pause