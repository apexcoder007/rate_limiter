import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.num_tokens = capacity
        self.last_lookup = time.time()

    def handle_request(self, token_per_request = 1):
        curr_time = time.time()
        time_elapsed = curr_time - self.last_lookup
        self.last_lookup = curr_time
        self.num_tokens = min(self.capacity, self.num_tokens + time_elapsed * self.refill_rate)

        if self.num_tokens >= token_per_request:
            self.num_tokens -= token_per_request
            print("Request routed successfully...")
        else:
            print("Too many requests!")

limiter = TokenBucket(3,1)

for _ in range(10):
    limiter.handle_request()
    time.sleep(0.1)