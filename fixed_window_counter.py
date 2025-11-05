import time

class fixedWindowCounter:
    def __init__(self, window_size, max_tokens):
        self.window_size = window_size
        self.max_tokens = max_tokens
        self.curr_window = time.time()//window_size
        self.request_cnt  = 0

    def handle_request(self):
        curr_time = time.time()
        curr_window = curr_time//self.window_size

        if curr_window != self.curr_window:
            self.curr_window = curr_window
            self.request_cnt = 0

        if self.request_cnt < self.max_tokens:
            self.request_cnt += 1
            print("Request routed successfully...")
            
        print("Request dropped!")

