# PyBruter
Basic login form bruteforcer 
***********************************************************
Usage:

Pretty straightforward, change the username to whatever user username you wish to attempt to brute force. For example purposes I am using the 'rockyou' wordlist which can also be found on github but feel free to replace that with whatever wordlist you feel appropriate. Also make note that I am making a POST request, you might also need to change this depending on the nature of how the login form works but it is safe to assume that a POST request will be what a site using HTTP will use to attempt to authenticate users. Also please note that the program tests for the string "Incorrect" in the string that is returned when a forbidden (error 403) request was made which may vary from site to site so before using this program you need to know what exactly the site returns with, I would suggest making a single POST request with false credentials and looking at the returned value. 

