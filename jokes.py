#------randome joke functions using different APIs
import requests
import random
def geeks():
    url = "https://geek-jokes.sameerkumar.website/api"
    resp = requests.get(url)
    resp.encoding = "utf-8"
    data = resp.json()
    return (data)

def chuck_norris():
  url = "https://api.icndb.com/jokes/random"
  resp = requests.get(url)
  resp.encoding = "utf-8"
  data = resp.json()
  return (data["value"]["joke"])

def stormconsultancy_quotes():
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    resp = requests.get(url)
    resp.encoding = "utf-8"
    data = resp.json()
    return (data["quote"])

def cat_fact_quotes():
    url = "https://cat-fact.herokuapp.com/facts/random"
    resp = requests.get(url)
    resp.encoding = "utf-8"
    data = resp.json()
    return (data["text"])

def get_msg():
    x = random.randint(0,3)
    if(x == 0):
        return (geeks())
    elif(x == 1):
        return (chuck_norris())
    elif(x == 2):
        return (stormconsultancy_quotes())
    elif(x == 3):
        return (cat_fact_quotes())
