class UserRequestHandler:
    def __init__(self, circuit_breaker, request_queue, backend_service):
        self.circuit_breaker = circuit_breaker
        self.request_queue = request_queue
        self.backend_service = backend_service

    def handle_request(self, request):
        if self.circuit_breaker.state == 'CLOSED':
            try:
                self.backend_service.process(request)
                self.circuit_breaker.success()
            except Exception:
                self.circuit_breaker.record_failure()
                self.request_queue.add_request(request)
        elif self.circuit_breaker.state == 'OPEN':
            self.request_queue.add_request(request)
        elif self.circuit_breaker.state == 'HALF_OPEN':
            try:
                self.backend_service.process(request)
                self.circuit_breaker.success()
            except Exception:
                self.circuit_breaker.failure()