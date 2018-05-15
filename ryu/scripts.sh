#!/bin/bash
curl -X POST -d ‘{“address”:”1.1.1.1/30”}’ http://localhost:8080/router/0000000000000001
curl -X POST -d ‘{“address”:”12.12.12.1/30”}’ http://localhost:8080/router/0000000000000001
curl -X POST -d ‘{“address”:”2.2.2.1/30”}’ http://localhost:8080/router/0000000000000002
curl -X POST -d ‘{“address”:”12.12.12.2/30”}’ http://localhost:8080/router/0000000000000002 
curl -X POST -d ‘{“address”:”3.3.3.1/30”}’ http://localhost:8080/router/0000000000000003
curl -X POST -d ‘{“address”:”12.12.12.3/30”}’ http://localhost:8080/router/0000000000000003 
curl -X POST -d ‘{“gateway”:”12.12.12.2”}’ http://localhost:8080/router/0000000000000001
curl -X POST -d ‘{“gateway”:”12.12.12.3”}’ http://localhost:8080/router/0000000000000002
curl -X POST -d ‘{“gateway”:”12.12.12.1”}’ http://localhost:8080/router/0000000000000003