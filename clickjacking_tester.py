#!/usr/bin/python3

import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

def clickjacking_test(url):
        try:
                request = urllib.request.Request(url)
                opener = urllib.request.urlopen(request)
        except URLError as error:
                print(error)
        except HTTPError as error:
                print(error)

        content = opener.headers
        print(opener.status, opener.reason)
        if content.__contains__("X-Frame-Options"):
                print("Framing is not allowed")
        else:
                print("Framing is allowed")

        resp_print = " "
        while resp_print not in ["y", "n"]:
                resp_print = input("Response shall be printed? (y/n) ")
                if resp_print == "y":
                        print(content)
                elif resp_print == "n":
                        print("Bye!")
                else:
                        print("Please, choose 'y' or 'n'!")


if __name__ == "__main__":
        host = input("Host url (eg. http://www.example.com): ")
        clickjacking_test(host)

