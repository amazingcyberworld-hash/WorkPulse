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
            print(f"[{datetime.now().strftime('%H:%M:%S')}] come back to work")
            self.is_idle = False  
    
    def check_idle(self):
        current_time = time.time() 
        elapsed_time = current_time - self.last_active_time 

        if elapsed_time > self.idle_threshold and not self.is_idle:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] leave, over {int(elapsed_time)}")
            self.is_idle = True 

    def start(self):
        mouse_listener = mouse.Listener(on_move = self.on_activity, on_click=self.on_activity, on_scroll=self.on_activity)
        key_listener = keyboard.Listener(on_press=self.on_activity)

        mouse_listener.start()
        key_listener.start() 

        print(f"start, {self.idle_threshold} seconds")

        try:
            while True:
                self.check_idle() 
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("exit monitoring")
            