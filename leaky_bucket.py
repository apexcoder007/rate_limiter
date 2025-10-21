from collections import deque
import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.bucket = deque()
        self.last_leak = time.time()

    def handle_request(self):
        curr_time = time.time()
        time_elapsed = curr_time - self.last_leak
        leaked_tokens_cnt = int(time_elapsed * self.leak_rate)

        if leaked_tokens_cnt > 0:
            for _ in range(min(leaked_tokens_cnt, len(self.bucket))):
                self.bucket.popleft()
            self.last_leak = curr_time
        
        if len(self.bucket) < self.capacity:
            self.bucket.append(curr_time)
            print("Request queued...")
        else:
            print("Request dropped...")