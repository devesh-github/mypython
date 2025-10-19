import time
import threading

class HealthCheckService:
    def __init__(self, circuit_breaker, check_interval):
        self.circuit_breaker = circuit_breaker
        self.check_interval = check_interval

    def check_service_health(self):
        while True:
            if self.circuit_breaker.state == 'OPEN':
                self.circuit_breaker.attempt_reset()
            time.sleep(self.check_interval)