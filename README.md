# echo-server with docker-compose in Python

This is the initial step towards writing a **Honeypot**. This repository contains an echo-server as _server.py_, a client as _client.py_ and a proxy as _proxy.py_ . The corresponding dockerfiles are maintained in **ServerDocker** and **ProxyDocker directories**.

The _server.py_ and _proxy.py_ files are run in containers using the _docker-compose.yml_ .This is a simple model which gives an idea on how a proxy can log all the informations that are passed from a client to server as it acts as an intermediate between client and proxy. _The Honeypot will work in the same manner_.
