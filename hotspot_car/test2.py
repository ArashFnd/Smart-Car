# import websocket
# import time
 

# def on_error(ws, error):
#     print(error)

# def on_message(ws, error):
#     print( error)

# def on_close(ws, error):
#     print( error)


# ws = websocket.WebSocket()
# ws.connect("ws://192.168.4.1/")
 
# i = 10
# while i:
#     try:
#         ws.send("Data")
#         result = ws.recv()
#         print(result)
#         time.sleep(0.1) 
#         i -= 1
#     except:
#         ws.connect("ws://192.168.4.1/")
 
# ws.close()




# import websocket
# import time
 
# ws = websocket.WebSocket()
# ws.connect("ws://192.168.4.1/")
 
# i = 0
# nrOfMessages = 30
 
# while i<nrOfMessages:
#     ws.send("Soft AP mode: message nr " + str(i))
#     result = ws.recv()
#     print(result)
#     i=i+1
#     time.sleep(1)
 
# ws.close()


import websocket
import time  

ws = websocket.WebSocket()
# ws.connect("ws://192.168.4.1/ws") #nodmcu hotspot
ws.connect("ws://192.168.1.9/ws")
while True:
    ws.send("nothing")
    result = ws.recv()
    print(result)
    time.sleep(0.1)
 
ws.close()