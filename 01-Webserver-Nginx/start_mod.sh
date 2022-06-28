sudo docker build -t webserver -f Dockerfile_mod .
echo "Running Docker"
docker run -i -d -p 80:80 webserver 
# goto http://localhost:80