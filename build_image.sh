#!/bin/bash

#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/aventuri/opencaster.git"
# Define the directory where you want to clone the repository
CLONE_DIR="."

# Check if the directory exists
# if [ ! -d "$CLONE_DIR" ]; then
#     # Directory doesn't exist, clone the repository
#     git clone "$REPO_URL" "$CLONE_DIR"
#     echo "opencaster cloned successfully."
# else
#     # Directory exists, check if it's a git repository
#     if [ -d "$CLONE_DIR/.git" ]; then
#         echo "opencaster repository already exists."
#     else
#         # Directory exists but not a git repository
#         echo "Error: $CLONE_DIR exists but is not a git repository."
#         exit 1
#     fi
# fi


# Criar imagem
DOCKER_BUILDKIT=1 docker build --progress=plain -t opencaster .

# --tag , -t		Name and optionally a tag in the name:tag format

# Fonte: https://docs.docker.com/engine/reference/commandline/build/