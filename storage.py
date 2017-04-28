from allegro.consumer import BaseConsumer

from pprint import pprint

class StorageManager(BaseConsumer):
    def __init__(self):
        super(TestConsumer, self).__init__()
        
    def post(self, message):
        pprint(message)
        return self._response("GET Received!!!", True)

    def patch(self, message):
        pprint(message)
        return self._response(resp, True)

    def put(self, message):
        pprint(message)
        return self._response(resp, True)

    def delete(self, message):
        pprint(message)
        return self._response(resp, True)

