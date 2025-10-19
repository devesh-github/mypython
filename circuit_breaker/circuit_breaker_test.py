import time
import threading

from circuit_breaker import CircuitBreaker
from health_check_service import HealthCheckService
from request_queue import RequestQueue
from backend_service import BackendService
from user_request_handler import UserRequestHandler

# Initialize components
circuit_breaker = CircuitBreaker(failure_threshold=1, recovery_timeout=2, half_open_retry_interval=1)
request_queue = RequestQueue()
backend_service = BackendService()  # Assume BackendService is defined elsewhere
user_request_handler = UserRequestHandler(circuit_breaker, request_queue, backend_service)
health_check_service = HealthCheckService(circuit_breaker, check_interval=1)

# Start health check service
health_check_thread = threading.Thread(target=health_check_service.check_service_health)
health_check_thread.start()

# Simulate handling requests
while True:
    request = backend_service.get_next_request  # Assume get_next_request() fetches the next user request
    user_request_handler.handle_request(request)
    time.sleep(1)  # Simulate time between requests