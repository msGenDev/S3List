#!/usr/bin/env python

"""Displays all download urls in a S3 Bucket."""

import S3
import httplib
import sys
import urllib
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
URL_PREFIX = '' #SOMETHING LIKE http://s3.amazonaws.com/marketcircle/ 

BUCKET_NAME = "marketcircle"

conn = S3.AWSAuthConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
response = conn.list_bucket(BUCKET_NAME)        
for en in response.entries:
    url = "%s%s" % (URL_PREFIX ,urllib.quote(en.key))
    print url
    