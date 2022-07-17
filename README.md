# opcua_client_python
A simple python OPC UA client. The client can be used to get data from an OPC UA server and as well set values for different on the server. 

# OPC UA Server
You can use the endpoint of your OPC UA server if you have one running already. A PROSYS Simulation server has been used in this implementation.
If you don't have a server running already, you can use a Server Simulation to test your client.
You can find the tutorial on how to install, configure and use a [PROSYS simulation server here](https://www.youtube.com/watch?v=jPnOJ3Z2c0I&t=90s)

# Install Dependencies
```
pip3 install -r requirements.txt
```
# How to get Nodes and Node values
1. replace the url value with your server endpoint
```
url = "opc.tcp://DESKTOP-FL73J86.mshome.net:53530/OPCUA/SimulationServer"
```
2. add the nodes you want to monitor. Specify the namespace (ns) and id (i) for each node
```
tempNode = client.get_node("ns=3;i=1001")
temperature = tempNode.get_value()
```

# How to set Node Values
1. create a node variable for a node on the server specifying the namespace (ns) and id (i) for the node
```
numNode = client.get_node("ns=3;i=1008")
```
2. set the value of the created node
```
client.set_values([numNode], [num+1])
```
