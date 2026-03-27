import time 
import requests
from pynput import mouse, keyboard 
from datetime import datetime 

class ActivityMonitor: 
    def __init__(self, emp_id ,idle_threshold):
        self.emp_id = emp_id
        self.idle_threshold = idle_threshold 
        self.last_active_time = time.time()
        self.is_idle = False 

    def send_to_server(self, status): 
        url = "http://127.0.0.1:5000/api/v1/activity"

        payload = {
            "emp_id": self.emp_id,
            "status": status,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        try: 
            response = requests.post(url, json=payload, timeout=3, verify=False) 

            if response.status_code == 200:
                print(f"success {status}")
            else:
                print(f"error {response.status_code}")

        except Exception as e:
            print(f"network error, fail to connect due to {e}")

    def on_activity(self, *args): 
        self.last_active_time = time.time() 
        if self.is_idle: 
            log_msg = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] come back to work"
            print(log_msg)
            self.save_to_log(log_msg)
            self.send_to_server("BACK")
            self.is_idle = False  
    
    def check_idle(self):
        current_time = time.time() 
        elapsed_time = current_time - self.last_active_time

        if elapsed_time > self.idle_threshold and not self.is_idle:
            log_msg = f"[{datetime.now().strftime('%H:%M:%S')}] leave, over {int(elapsed_time)}"
            
            print(log_msg)
            self.save_to_log(log_msg)
            self.send_to_server("LEAVE")
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