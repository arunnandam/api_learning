from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

# Define the directory where your JSON file is located
DIRECTORY = '.'  # Assuming the JSON file is in the current directory
# Define the port on which the server will listen
PORT = 8000

# HTTPRequestHandler class
class HTTPRequestHandler(SimpleHTTPRequestHandler):
    # Override the do_GET method to serve the JSON file
    def do_GET(self):
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Open and read the JSON file
        with open('students.json', 'rb') as file:
            self.wfile.write(file.read())

    def do_GET_byId(self,id):
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Open and read the JSON file
        with open('students.json', 'r') as file:
            data = json.load(file)

        self.wfile.write(data[id])

        


# Create an HTTP server
httpd = HTTPServer(('', PORT), HTTPRequestHandler)

# Print a message indicating the server is running
print(f'Server running on port {PORT}...')

# Start the server
httpd.serve_forever()
