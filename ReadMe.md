# Some inspiration from
https://training.play-with-docker.com/beginner-linux/

# Dockerfile commands
https://docs.docker.com/engine/reference/builder/

# List all docker images
docker images 

# view running dockers
 docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
 docker ps --format "table {{.ID}}\t{{.Ports}}\t{{.Names}}\t{{.Status}}"
 https://docs.docker.com/engine/reference/commandline/ps/


# Stop all running Docker containers
docker kill $(docker ps -q)

# Delete all containers not running
docker system prune

# Attach VSCode to running container
https://code.visualstudio.com/docs/remote/attach-container

# Docker compose
docker-compose --profile airflow up
