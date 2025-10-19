from queue import Queue

class RequestQueue:
    def __init__(self):
        self.queue = Queue()

    def add_request(self, request):
        self.queue.put(request)

    def process_requests(self, backend_service):
        while not self.queue.empty():
            request = self.queue.get()
            backend_service.process(request)