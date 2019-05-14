#!/usr/bin/env python3


import urllib.request
import urllib.parse

def read_text():
    #quotes = open("movie_quotes.txt")  # Returns a `file` object
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check, 'utf-8')
    address = "http://www.wdylike.appspot.com/?q="+encoded_text
    print(address)
    connection = urllib.request.urlopen(address)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("There is no curse word in file")
    else:
        print("Unable to scan document properly")

read_text()
