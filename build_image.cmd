@ECHO OFF

REM Check if Docker Desktop is running
docker ps -q >nul 2>&1
IF ERRORLEVEL 1 (
  ECHO Error: Docker Desktop is not running. Please start it and try again.
  EXIT /B 1
)

REM Build the image with progress output
set DOCKER_BUILD=1
docker build -t opencaster . --progress=plain

IF ERRORLEVEL 1 (
  ECHO Error: Image build failed. Check the Docker output for details.
  EXIT /B 1
)

ECHO Image build completed successfully.