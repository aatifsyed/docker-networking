# Create network
```
docker network create --driver bridge aatif.net
```
# Build container
```
docker build --tag dataserver . && docker image prune
```
# Run server
```
docker run --rm --interactive --tty --hostname server --name server --network aatif.net dataserver
```