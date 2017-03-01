from txrequest import txRequest, ResponseProtocol
from twisted.internet.defer import Deferred

class ExampleProtocol(ResponseProtocol):
	
	def handleData(self):
		"""
		Handle the GET request's data held in self.body
		"""
		print self.body
		pass
			
def callback(response):
    finished = Deferred()
    response.deliverBody(ExampleProtocol(finished))
    return finished

txRequest('http://coinmarketcap.com/currencies/bitcoin/', callback)
