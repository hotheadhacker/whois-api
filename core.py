import whois
import datetime
w = whois.whois('salmanually.com')
w.expiration_date  # dates converted to datetime object
datetime.datetime(2013, 6, 26, 0, 0)
w.text  # the content downloaded from whois server u'\nWhois Server Version 2.0\n\nDomain names in the .com and .net'

print(w)  # print values of all found attributes
