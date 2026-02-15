# bookapidao.py
# Module to interact with API
# Author: Daniel Finnerty

import requests
import json
URL = 'http://andrewbeatty1.pythonanywhere.com/books'

'''
url = "http://google.com" 
response = requests.get(url) 
print (response.text)
'''

# response = requests.get(URL) 
# print (response.json())

def readbooks(): 
    response = requests.get(URL) 
    return response.json() 

# Check for correct response code 
# if __name__ == "__main__": 
    # print (readbooks())


def readbook(id): 
    geturl = URL + "/" + str(id) 
    response = requests.get(geturl) 
    return response.json()

# Check for correct response code
# if __name__ == "__main__": 
    # print (readbook(1626))


def createbook(book): 
    book = {
        "Author":"test",
        "title":"test again",
        "price":"119"
    }
    response = requests.post(URL, json=book) 
    return response.json()

# Checking the correct status code 
if __name__ == "__main__": 
    book = {
        "Author": "test",
        "title": "test again",
        "price": "119"
    }
    print (createbook(book))
