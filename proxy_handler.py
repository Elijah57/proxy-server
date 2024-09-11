from urllib import  request; # for making request
from http import server; # a basic http server



# Defining a proxy request handler
#  A Proxy server that handles request

class Proxy(server.SimpleHTTPRequestHandler): #inherit, the basic HTTP request handler
    def do_GET(self): #overriding the handler for Get request

        #step 1, get the target url from the request path
        # examaple, self.path is "/http://example.com"
        target_url = self.path[1:]
        print(f"Feting: {target_url}")


        try:
            #make a request to the target url
            response = request.urlopen(target_url)
            self.send_response(response.getcode())

            #send headers
            self.send_header("Content-type", response.info().get_content_type())
            self.end_headers()

            #send the content of the response
            self.wfile.write(response.read())

        except:
            self.send_error(404, f"Error fetching {target_url}")

