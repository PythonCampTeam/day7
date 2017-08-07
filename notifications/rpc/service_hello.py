from nameko.rpc import rpc

class GreetingService(object):
    name = 'greeting_service'

    @rpc
    def hello(self, name):
        return 'Hello padla {}!!!!'.format(name)
