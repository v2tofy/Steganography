@echo off
title Steganography Tool

echo [*] Checking dependencies...
pip install -r requirements.txt >nul 2>&1

echo [*] Launching tool...
python src\main.py

pause
