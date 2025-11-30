@echo off
python -m pytest -v -s --html=Reports\report.html Testcases\test_logindd.py --browser chrome
pause
