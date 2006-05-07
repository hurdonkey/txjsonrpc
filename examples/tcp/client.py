import os
import sys
sys.path.insert(0, os.getcwd())

from twisted.internet import reactor
try:
    from adytum.twisted.jsonrpc import Proxy
except ImportError:
    from pkg_resources import require
    require('Twisted-JSONRPC')
    from adytum.twisted.jsonrpc import Proxy

def printValue(value):
    print "Result: %s" % str(value)
    reactor.stop()

def printError(error):
    print 'error', error
    reactor.stop()

print "Making remote call..."
proxy = Proxy('127.0.0.1', 7080)
proxy.callRemote('add', 3, 5).addCallbacks(printValue, printError)
reactor.run()

