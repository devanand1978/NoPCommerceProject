@ECHO OFF
ECHO "RUNIING TESTCASES....."
pytest -s -v -m "sanity and regression" --html=./Reports/report.html TestCases/ --browser=chrome
pytest -s -v -m "sanity and regression" --html=./Reports/report.html TestCases/ --browser=firefox
REM pytest -s -v -m "sanity" --html=./Reports/report.html TestCases/ --browser=chrome
REM pytest -s -v -m "regression" --html=./Reports/report.html Testcases/ --browser=chrome
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html Testcases/ --browser=chrome
PAUSE