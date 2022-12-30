#! usr/bin/bash

service=demo

docker swarm init

docker stack deploy -c docker-compose.yaml $service