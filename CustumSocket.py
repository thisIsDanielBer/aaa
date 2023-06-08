import base64
import socket


class CustumSocket:
   my_socket = socket.socket()

   def __init__(self):
       pass

   def sendto(self, message, remote_socket):
       
       message_bytes = message.encode('ascii')
       base64_bytes = base64.b64encode(message_bytes)
       self.my_socket.connect(remote_socket)
       self.my_socket.send(base64_bytes)
       print("Sent to server " + str(len(base64_bytes)) + "bytes")
       base64_ack = self.my_socket.recv(1024)
       ack_bytes = base64.b64decode(base64_ack)
       ack = ack_bytes.decode('ascii')
       print("server recived " + ack + "bytes")

   def recvfrom(self, buffer_size):
       
       self.my_socket.bind(("0.0.0.0", 12345))
       self.my_socket.listen(2)
       conn, address = self.my_socket.accept()
       base64_bytes = conn.recv(buffer_size)
       message_bytes = base64.b64decode(base64_bytes)
       message = message_bytes.decode('ascii')
       recived = str(len(base64_bytes))
       ack = recived.encode()
       base64_ack = base64.b64encode(ack)
       conn.send(base64_ack)
       return message
   
