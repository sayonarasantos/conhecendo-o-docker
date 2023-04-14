docker pull dpage/pgadmin4
docker image ls
docker run -e PGADMIN_DEFAULT_EMAIL=email@email.com -e PGADMIN_DEFAULT_PASSWORD=1234 -p 8080:80 -d --name pgadmin dpage/pgadmin4
docker ps
docker logs pgadmin 
docker ps -a
docker container prune