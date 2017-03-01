from txrequest import txRequest, ResponseProtocol
from twisted.internet.defer import Deferred

class ExampleProtocol(ResponseProtocol):
	"""
	Override the empty built in ResponseProtocol.handleData method to do something
	"""
	def handleData(self):
		"""
		Handle the GET request's data held in self.body
		"""
		print self.body
		pass
			
def callback(response):
	"""The callback which executes your protocol to handle
	the data once the request is made
	"""
    finished = Deferred()
    response.deliverBody(ExampleProtocol(finished))
    return finished

txRequest('http://coinmarketcap.com/currencies/bitcoin/', callback)
