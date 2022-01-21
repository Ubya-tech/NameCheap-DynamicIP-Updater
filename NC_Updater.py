import requests
import dotenv
import os

#https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-to-dynamically-update-the-hosts-ip-with-an-http-request/

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file) #finds .env file in the same directory of this script, and loads it

old_ip = os.environ["PUBLIC_IP"]
new_ip = requests.get('https://api.ipify.org?format=json').json()['ip'] #checks your current public ip, you can't see your public ip locally

if old_ip != new_ip:
        payload = {
        "host":os.environ["HOST"],
        "domain":os.environ["DOMAIN"],
        "password":os.environ["DDNS_PASSWORD"],
        "ip":new_ip
        }
        update = requests.get("https://dynamicdns.park-your-domain.com/update", params=payload)
        #print(update.url) #to check if the URL is right (https://dynamicdns.park-your-domain.com/update?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip])
        os.environ["PUBLIC_IP"] = new_ip
        dotenv.set_key(dotenv_file, "PUBLIC_IP", os.environ["PUBLIC_IP"]) #updating the enviroment variable with the new ip
