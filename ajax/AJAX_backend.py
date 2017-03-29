from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SimpleHTTPServer

PORT = 10125

class AjaxHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""
    def do_POST(self):
        """Handle a post request by returning the square of the number."""
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        # Send the html message
        self.wfile.write("Aivis Panovs, 161REB125")
        return

try:
    server = HTTPServer (('', PORT),AjaxHandler)
    print 'Started AJAX handler on port', PORT
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down server'
    server.socket.close()

