import configparser 
from ActiveMonitor import ActivityMonitor

config = configparser.ConfigParser()
config.read('config.ini')

emp_id = config['SETTINGS']['EMP_ID']
idle_threshold = int(config['SETTINGS']['IDLE_THRESHOLD'])

print(f"社員番号 [{emp_id}]を読み取りました.")
print(f"IDLE_THRESHOLD [{emp_id}]を読み取りました.")

monitor = ActivityMonitor(idle_threshold)
monitor.start()