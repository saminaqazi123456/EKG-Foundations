sudo docker build -t lunix .
echo "Running Docker"
docker run -i -d lunix 
# docker exec -it d8 /bin/bash     