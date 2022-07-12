# opcua_client_python
A simple python OPC UA client

# OPC US Server
You can use the endpoint of your OPC UA server if you have one running already. A PROSYS Simulation server has been used in this implementation.
If you don't have a server running already, you can use a Server Simulation to test your client.
You can find the tutorial on how to install, configure and use a [PROSYS simulation server here](https://www.youtube.com/watch?v=jPnOJ3Z2c0I&t=90s)

# Install Dependencies
```
pip3 install -r requirements.txt
```
# 
1. replace the url value with your server endpoint
2. add the nodes you want to monitor. specify the namespace (ns) and id(i) for each node
