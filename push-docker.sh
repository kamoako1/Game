#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=rpsgame .


dockerpath="kail2/rpsgame"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag rpsgame $dockerpath

# Push Image
docker image push $dockerpath 