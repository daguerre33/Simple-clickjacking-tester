#!/usr/bin/python3

import urllib.request

def clickjacking_test(url):
        request = urllib.request.Request(url)
        opener = urllib.request.urlopen(request)
        print(opener.status, opener.reason)
        if opener.headers.__contains__("X-Frame-Options"):
                print("Framing is not allowed")
        else:
                print("Framing is allowed")

if __name__ == "__main__":
        host = input("Host url (eg. http://example.com): ")
        clickjacking_test(host)

        
