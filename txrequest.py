from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet.protocol import Protocol

success = 'Response body fully received'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0'

class ResponseProtocol(Protocol):

    def __init__(self, finished):
        self.finished = finished
        self.body = ''

    def dataReceived(self, bytes):
        self.body += bytes
        
    def connectionLost(self, reason):
		if reason.getErrorMessage() != success:
			self.finished.callback(self.error(reason))
		else:
			self.finished.callback(self.handleData())

    def handleData(self):
		pass

    def error(reason):
        print reason.getErrorMessage()

def cbShutdown(_):
    reactor.stop()

def txRequest(host, callback, num_of_connections=1):
    agent = Agent(reactor)
    for i in xrange(num_of_connections):
       d = agent.request('GET', host, Headers({'User-Agent': [user_agent]}), None)
       d.addCallback(callback)
    d.addBoth(cbShutdown)
    reactor.run()

