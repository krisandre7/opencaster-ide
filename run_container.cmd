@ECHO OFF

REM Check if the image opencaster is present
@REM build_image.cmd  (Assuming build_image.cmd is a separate script or available)

REM Check if the opencaster-ide container is running
FOR /F "tokens=*" %%a IN ('docker container ls -a ^| findstr /i /c:"opencaster-ide"') DO (
  IF "%%a"=="opencaster-ide" (
    ECHO Started opencaster-ide
    ECHO To enter container, use docker exec -it opencaster-ide bash
  ) ELSE (
    REM Create and start the opencaster-ide container
    docker container run -dit --name opencaster-ide -v %cd%:/opencaster-ide opencaster
    ECHO Running opencaster-ide
    ECHO To enter container, use docker exec -it opencaster-ide bash
  )
)

REM Removed commented out container stop and removal lines as they are not recommended within the script

REM Reference: https://docs.docker.com/engine/reference/run/
