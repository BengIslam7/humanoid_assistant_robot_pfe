import paho.mqtt.client as paho
from paho import mqtt
import os
import time
client = paho.Client()
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("hivemq.webclient.1745834546662", "Fge.w;f!d36OW#4T9AYn")
client.connect("3a06204e5f944e08b8d312754d3f8ec7.s1.eu.hivemq.cloud", 8883)
cmd1 = 'ros2 topic pub /diff_cont/cmd_vel_unstamped geometry_msgs/msg/Twist "{linear: {x: '
cmd2 = ', y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: '
cmd3 = '}}" --once'

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    mp=msg.payload.decode('utf-8')
    print(mp)
    if(str(msg.payload)=="b'A'"):
        client.publish("pos", payload="A", qos=1)
    elif(str(msg.payload)=="b'B'"):
    	client.publish("pos", payload="B", qos=1)
    elif(str(msg.payload)=="b'H'"):
    	print(str(msg.payload)[2])
    	client.publish("pos", payload="H", qos=1)
    elif(mp[0]=="i"):
    	linear=mp.split(' ')[1]
    	angular='0.0'
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="u"):
    	linear=mp.split(' ')[1]
    	angular=mp.split(' ')[2]
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="o"):
    	linear=mp.split(' ')[1]
    	angular=mp.split(' ')[2]
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="k"):
    	linear='0.0'
    	angular='0.0'
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="j"):
    	linear='0.0'
    	angular=mp.split(' ')[1]
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="l"):
    	linear='0.0'
    	angular=mp.split(' ')[1]
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="m"):
    	linear=mp.split(' ')[1]
    	angular=mp.split(' ')[2]
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]=="."):
    	linear=mp.split(' ')[1]
    	angular=mp.split(' ')[2]
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    elif(mp[0]==","):
    	linear=mp.split(' ')[1]
    	angular='0.0'
    	pub=cmd1+linear+cmd2+angular+cmd3
    	print(pub)
    	os.system(pub)
    
    	

client.on_subscribe = on_subscribe
client.on_message = on_message
client.subscribe('dest', qos=1)
client.subscribe('cmd', qos=1)
client.loop_forever()

