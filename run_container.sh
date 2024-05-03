#!/bin/bash

# Check if the image opencaster is present
./build_image.sh

#Subir o ambiente do Banco de Dados Relacional MySQL
result=$(docker container ls -a | grep opencaster-ide)
container_name='opencaster-ide'

# verificar se o container opencaster-ide já foi criado
if [[ "$result" == *"$container_name"* ]]; 
then
    # apenas inicializa o container caso já esteja criado
    docker container start $container_name
    echo Started $container_name
    echo To enter container, use docker exec -it $container_name bash
    # docker exec -it $container_name bash
    echo To enter container, use "docker exec -it $container_name bash"
else
    # cria o container caso não foi criado
    docker container run -dit --name $container_name -v $(pwd):/$container_name opencaster
    echo Running $container_name
    echo To enter container, use "docker exec -it $container_name bash"
    # docker exec -it $container_name bash
fi

# # --name    nome do container
# # -v        mapear volume local:dentro_container
# # -it       modo iterativo, ou seja, permite entrar no container em modo console
# # -p        externalizar uma porta para acesso internamente ao container

# docker container stop opencaster-ide
# docker container rm -f opencaster-ide


# rm -f     apaga um container (-f )

# Fonte: https://docs.docker.com/engine/reference/run/