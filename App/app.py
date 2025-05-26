import tkinter as tk
from tkinter import PhotoImage
import paho.mqtt.client as paho
from paho import mqtt
import datetime
import time
title="Robot assistant"
title2="RobotApp"
global client
client = paho.Client(client_id='55', clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("hivemq.webclient.1745834546662", "Fge.w;f!d36OW#4T9AYn")
co=client.connect("3a06204e5f944e08b8d312754d3f8ec7.s1.eu.hivemq.cloud", 8883)
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    poslabel.config(text="Robot Position = "+str(payload))
client.on_subscribe = on_subscribe
client.on_message = on_message
client.subscribe('pos', qos=1)
client.loop_start()

def A(event):
    x=client.publish("dest", payload="A", qos=1)
    print(x)
def B(event):
    x=client.publish("dest", payload="B", qos=1)
    print(x)
def Home(event):
    x=client.publish("dest", payload="H", qos=1)
    print(x)

def forwardl(event):
    value = linear_vel.get()
    value2 = angular_vel.get()
    cmd="u "+value+" "+value2
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def forward(event):
    value = linear_vel.get()
    cmd="i "+value
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def forwardr(event):
    value = linear_vel.get()
    value2 = angular_vel.get()
    cmd="o "+value+" "+value2
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def stop(event):
    cmd="k"
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def left(event):
    value2 = angular_vel.get()
    cmd="j "+value2
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def right(event):
    value2 = angular_vel.get()
    cmd="l "+value2
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def backwardr(event):
    value = linear_vel.get()
    value2 = angular_vel.get()
    cmd=". "+value+" "+value2
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def backwardl(event):
    value = linear_vel.get()
    value2 = angular_vel.get()
    cmd="m "+value+" "+value2
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)
    
def backward(event):
    value = linear_vel.get()
    cmd=", "+value
    print(cmd)
    x=client.publish("cmd", payload=cmd, qos=1)
    print(x)

root = tk.Tk()
root.title(title)
root.geometry("400x550")
frame = tk.Frame(root)
l2 = tk.Label(root, width=27, text=title2,font=("Arial", 20),foreground="blue")
l2.pack(pady=5)
image_path = "robotapp.png"  # Change this to the path of your image file
img = PhotoImage(file=image_path)
# Create a label and set the image
label = tk.Label(root, image=img)
label.pack()
poslabel = tk.Label(root, width=27, text="Robot Position = Home",font=("Arial", 15))
poslabel.pack(pady=5)
button = tk.Button(frame, text="Home")
button2 = tk.Button(frame, text="A")
button3 = tk.Button(frame, text="B")
button.bind("<Button-1>", Home)
button2.bind("<Button-1>", A)
button3.bind("<Button-1>", B)
dest = tk.Label(root, width=27, text="Destination",font=("Arial", 15),foreground="blue")
dest.pack(pady=5)
button.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=10)
button3.pack(pady=10)
#control
line1 = tk.Frame(root)
line2 = tk.Frame(root)
line3 = tk.Frame(root)
ctr = tk.Label(line1, width=27, text="Controle",font=("Arial", 15),foreground="blue")
ctr.pack(pady=5)
linear_vel = tk.Entry(line1, width=10)
angular_vel = tk.Entry(line1, width=10)
linear_vel.pack(padx=10, pady=10)
angular_vel.pack(padx=10, pady=10)
# Define buttons
fwdl = tk.Button(line1, text="↖")
fwd = tk.Button(line1, text="↑")
fwdr = tk.Button(line1, text="↗")
bleft = tk.Button(line2, text="←")
bstop = tk.Button(line2, text="■")
bright = tk.Button(line2, text="→")
bwdl = tk.Button(line3, text="↙")
bwd = tk.Button(line3, text="↓")
bwdr = tk.Button(line3, text="↘")
fwdl.pack(side=tk.LEFT, padx=40,pady=10)
fwdl.bind("<Button-1>", forwardl)

fwd.pack(side=tk.LEFT, padx=40,pady=10)
fwd.bind("<Button-1>", forward)

fwdr.pack(side=tk.LEFT, padx=40,pady=10)
fwdr.bind("<Button-1>", forwardr)

bleft.pack(side=tk.LEFT, padx=40)
bleft.bind("<Button-1>", left)

bstop.pack(side=tk.LEFT, padx=40)
bstop.bind("<Button-1>", stop)

bright.pack(side=tk.LEFT, padx=40)
bright.bind("<Button-1>", right)

bwdl.pack(side=tk.LEFT, padx=40,pady=10)
bwdl.bind("<Button-1>", backwardl)

bwd.pack(side=tk.LEFT, padx=40,pady=10)
bwd.bind("<Button-1>", backward)

bwdr.pack(side=tk.LEFT, padx=40,pady=10)
bwdr.bind("<Button-1>", backwardr)

frame.pack()
line1.pack()
line2.pack()
line3.pack()
root.mainloop()
