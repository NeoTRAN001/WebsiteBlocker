import time
from datetime import datetime as dt

# host File
# windows C:\\windows\system32\drivers\etc
# linux & mac /etc/hosts

hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_unix = "/etc/hosts"
host_dir = hosts_path_unix

redirect = "127.0.0.1"  

website_list = [
    "youtube.com",
    "https://www.youtube.com/",
    "facebook.com",
    "amino.com"
]

from_hour = 9
to_hour = 10

while True:
    if from_hour < dt.now().hour < to_hour:
        print("Work...")
        with open(host_dir, 'r+') as file:
            content = file.read()
            
            for website in website_list:
                if not(website in content):
                    file.write(redirect + " " + website + "\n")
    else:
        print("fun...")
        with open(host_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(1)