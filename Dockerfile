# syntax=docker/dockerfile:1

FROM debian:buster
ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /opencaster-ide
RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean \
    && apt-get update && apt-get install -y --no-install-recommends \
    binutils gcc libc6-dev libgomp1 linux-libc-dev make python-dev zlib1g-dev python-dateutil \
    git dpkg wget curl dvbsnoop
ENV DEBIAN_FRONTEND=dialog 