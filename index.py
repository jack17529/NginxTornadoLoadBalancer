import tornado.web
import tornado.ioloop
import sys
import os

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        pid = str(os.getpid())
        self.write(pid)
        pass

"""
class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write("Querying tweet with id " + id)

class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "odd" if n % 2 else "even"
        
        self.write("the number " + str(n) + " is " + r)

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
"""

if (__name__ == "__main__"):
    print(os.getpid())
    app = tornado.web.Application([(r"/basic", basicRequestHandler)])

    port = 8882
    if(sys.argv.__len__()>1):
	    port = sys.argv[1]

    app.listen(port)
    print("I'm listening on ",port," port")
    tornado.ioloop.IOLoop.current().start()
