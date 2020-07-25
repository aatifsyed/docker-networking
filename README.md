# Create network
```
docker network create --driver bridge aatif.net
```
# Build container
```
docker container stop --time 0 server; docker build --tag dataserver . && docker image prune --force
```
# Run server
```
docker run --rm --interactive --tty --hostname server --name server --network aatif.net dataserver
```
## Attach to running server
```
docker exec --interactive --tty server bash
```
# Run client
```
docker run --rm --interactive --tty --hostname client --name client --network aatif.net dataserver ipython --pprint -i client.py
```