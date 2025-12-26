@echo off
pushd "%~dp0"
speedtest.exe --accept-license --accept-gdpr --format=csv >> ".\Data Files\Speedtest Monitoring.csv" 2>&1
popd