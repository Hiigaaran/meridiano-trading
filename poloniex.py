import urllib

import urllib2

import json

import time

import hmac,hashlib



def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):

    return time.mktime(time.strptime(datestr, format))