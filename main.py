import configparser 

config = configparser.ConfigParser()
config.read('config.ini')

emp_id = config['SETTINGS']['EMP_ID']
print(f"🎉 社員番号 [{emp_id}]を読み取りました.")

