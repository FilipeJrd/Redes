#!/bin/bash
curl -X POST -d '{"address":"1.1.1.1/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d '{"address":"12.12.12.1/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d '{"address":"2.2.2.1/30"}' http://localhost:8080/router/0000000000000002
curl -X POST -d '{"address":"12.12.12.2/30"}' http://localhost:8080/router/0000000000000002 
curl -X POST -d '{"address":"3.3.3.1/30"}' http://localhost:8080/router/0000000000000003
curl -X POST -d '{"address":"12.12.12.3/30"}' http://localhost:8080/router/0000000000000003 
curl -X POST -d '{"gateway":"12.12.12.2"}' http://localhost:8080/router/0000000000000001
curl -X POST -d '{"gateway":"12.12.12.3"}' http://localhost:8080/router/0000000000000002
curl -X POST -d '{"gateway":"12.12.12.1"}' http://localhost:8080/router/0000000000000003

curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
curl -X POST -d '{"nw_src": "1.1.1.3/30", "nw_dst": "2.2.2.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "1.1.1.3/30", "nw_dst": "2.2.2.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"nw_src": "1.1.1.3/30", "nw_dst": "2.2.2.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000003

curl -X POST -d '{"nw_src": "2.2.2.3/30", "nw_dst": "1.1.1.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "2.2.2.3/30", "nw_dst": "1.1.1.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"nw_src": "2.2.2.3/30", "nw_dst": "1.1.1.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000003

curl -X POST -d '{"nw_src": "1.1.1.3/30", "nw_dst": "3.3.3.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "1.1.1.3/30", "nw_dst": "3.3.3.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"nw_src": "1.1.1.3/30", "nw_dst": "3.3.3.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000003


curl -X POST -d '{"nw_src": "3.3.3.3/30", "nw_dst": "1.1.1.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "3.3.3.3/30", "nw_dst": "1.1.1.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"nw_src": "3.3.3.3/30", "nw_dst": "1.1.1.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000003


curl -X POST -d '{"nw_src": "2.2.2.3/30", "nw_dst": "3.3.3.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "2.2.2.3/30", "nw_dst": "3.3.3.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"nw_src": "2.2.2.3/30", "nw_dst": "3.3.3.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000003

curl -X POST -d '{"nw_src": "3.3.3.3/30", "nw_dst": "2.2.2.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "3.3.3.3/30", "nw_dst": "2.2.2.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"nw_src": "3.3.3.3/30", "nw_dst": "2.2.2.3/30", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000003
