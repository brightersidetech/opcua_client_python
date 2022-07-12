import sys
from opcua import Client
import time

url = "opc.tcp://DESKTOP-FL73J86.mshome.net:53530/OPCUA/SimulationServer"
if __name__ == '__main__':
    try:
        client = Client(url)
        client.connect()
        print("Connected to OPC UA Server")
    except Exception as err:
        print("server not found")
        sys.exit(1)

    # get node data from your server
    while True:
        # get nodes and node data from the server
        tempNode = client.get_node("ns=3;i=1001")
        temperature = tempNode.get_value()
        print("Temperature: ", temperature)

        numNode = client.get_node("ns=3;i=1008")
        num = numNode.get_value()
        print("Number: ", num)

        # Set a node values
        client.set_values([numNode], [num+1])
        time.sleep(2)
