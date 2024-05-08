REM Check if the image opencaster is present
call build_image.cmd

REM Subir o ambiente do Banco de Dados Relacional MySQL
for /f "tokens=*" %%a in ('docker container ls -a ^| findstr /C:"opencaster-ide"') do set result=%%a
set container_name=opencaster-ide

REM verificar se o container opencaster-ide já foi criado
if not "%result%"=="" (
    REM apenas inicializa o container caso já esteja criado
    docker container start %container_name%
    echo Started %container_name%
    echo To enter container, use docker exec -it %container_name% bash
    REM docker exec -it %container_name% bash
    echo To enter container, use "docker exec -it %container_name% bash"
) else (
    REM cria o container caso não foi criado
    docker container run -dit --name %container_name% -v %cd%:/%container_name% opencaster
    echo Running %container_name%
    echo To enter container, use "docker exec -it %container_name% bash"
    REM docker exec -it %container_name% bash
)
