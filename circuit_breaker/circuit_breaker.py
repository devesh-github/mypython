import time


class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_timeout, half_open_retry_interval):
        self.state = 'CLOSED'
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_retry_interval = half_open_retry_interval
        self.last_failure_time = None

    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'

    def reset(self):
        self.failure_count = 0
        self.state = 'CLOSED'

    def attempt_reset(self):
        if self.state == 'OPEN' and (time.time() - self.last_failure_time) >= self.recovery_timeout:
            self.state = 'HALF_OPEN'

    def success(self):
        if self.state == 'HALF_OPEN':
            self.reset()

    def failure(self):
        if self.state == 'HALF_OPEN':
            self.state = 'OPEN'
            self.last_failure_time = time.time()