import urllib.request
import os
# import pandas as pd # pip install pandas openpyxl
# from pushbullet import Pushbullet # pip install pushbullet.py
import ssl
# import urllib.request as urlrq
import certifi

# import requests
# requests.packages.urllib3.disable_warnings()

# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     ssl._create_default_https_context = _create_unverified_https_context

# # ssl._create_default_https_context = ssl._create_unverified_context
# # API KEY PushBullet (https://www.pushbullet.com/)
# # API_KEY = "o.M6oobwiMGWdRR5SDlGmtb2YAdmh3Ksnb"
# API_KEY = "o.0hD1MGYRjGabzRY6ASIX6vKOmMTon7gZ"


# Get Link to Chatfile from Pushbullet
# pb = Pushbullet(API_KEY)
# pushes = pb.get_pushes()
# latest = pushes[0]

def getchat():
    # Download Chatfile
    # url = latest['file_url']
    file_path = "chat.txt"
    # context = ssl._create_unverified_context()
    # urllib.request.urlretrieve(url, file_path)

    # read file by lines
    with open(file_path, mode='r', encoding="utf8") as f:
        data = f.readlines()

    # FOUND ON GITHUB: https://gist.github.com/kwcooper/a21ba58272d3cdf26310cc02ee4b168f
    # parse text, create list of lists structure & remove first whatsapp info message
    dataset = data[1:]
    cleaned_data = []
    for line in dataset:
        # Check, whether it is a new line or not
        # If the following characters are in the line -> assumption it is NOT a new line
        if '/' in line and ':' in line and ',' in line and '-' in line:
            # grab the info and cut it out
            date = line.split(",")[0]
            line2 = line[len(date):]
            time = line2.split("-")[0][2:]
            line3 = line2[len(time):]
            name = line3.split(":")[0][4:]
            line4 = line3[len(name):]
            message = line4[6:-1] # strip newline charactor
            if message and "https:" in message and "Engagement" not in message:
                cleaned_data.append(message)

        # else, assumption -> new line. Append new line to previous 'message'
        # else:
        #     new = cleaned_data[-1][-1] + " " + line
        #     cleaned_data[-1][-1] = new
    return cleaned_data
    # Create the DataFrame
    # print("message-------------------------------------------------------",cleaned_data)

# df = pd.DataFrame(cleaned_data, columns = ['Message'])

# Save it!
# df.to_excel('chat_history.xlsx', index=False)