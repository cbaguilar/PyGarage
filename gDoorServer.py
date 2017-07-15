import socketserver
import time

LIB = False

try:
    import RPi.GPIO as gp
    LIB = True
    print("Loaded GPIO library")
    gp.setmode(gp.BOARD)
    gp.setup(16,gp.OUT)
    gp.output(16,1)
except Exception:
    LIB = False
    print("Could not load GPIO library")

def lift():
    print("Lifting...")
    if LIB:
        gp.output(16,0)
        time.sleep(0.5)
        gp.output(16,1)
    else:
        print("No GPIO, simulating lift...")

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data.decode())
        lift()
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "192.168.2.100", 31415

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    print("Starting server")
    for x in range(0,9):
        print(x)
    