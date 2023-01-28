#!/usr/bin/env bash

# Build
docker build --tag cli-tool .

# List containers
docker image ls
