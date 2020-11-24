This is a project create an API using the Django and python framework.  


(Note: assumes you have a docker dameon running) 
Linux add the sudo command, mac don't need that. 
To build the docker container: 

sudo docker build -t djangoapi .

to run docker container:
sudo docker run -it -p 8000:8000 djangoapi

to stop:

find the container id
sudo docker ps -a

sudo docker stop <containerID>


