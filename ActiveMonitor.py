import time 
from pynput import mouse, keyboard 
from datetime import datetime 

class ActivityMonitor: 
    def __init__(self, idle_threshold):
        self.idle_threshold = idle_threshold 
        self.last_active_time = time.time()
        self.is_idle = False 

    def on_activity(self, *args): 
        self.last_active_time = time.time() 
        if self.is_idle: 
            log_msg = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] come back to work"
            print(log_msg)
            self.save_to_log(log_msg)
            self.is_idle = False  
    
    def check_idle(self):
        current_time = time.time() 
        elapsed_time = current_time - self.last_active_time

        if elapsed_time > self.idle_threshold and not self.is_idle:
            log_msg = f"[{datetime.now().strftime('%H:%M:%S')}] leave, over {int(elapsed_time)}"
            
            print(log_msg)
            self.save_to_log(log_msg)
            self.is_idle = True 

    def start(self):
        
        mouse_listener = mouse.Listener(on_move = self.on_activity, on_click=self.on_activity, on_scroll=self.on_activity, daemon=True)
        key_listener = keyboard.Listener(on_press=self.on_activity, daemon = True)

        mouse_listener.start()
        key_listener.start() 

        print(f"start, {self.idle_threshold} seconds")

        try:
            while True:
                self.check_idle() 
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("exit monitoring")

    def save_to_log(self, message):
        with open("work_log.txt", "a", encoding="utf-8") as f: 
            f.write(message + "\n")