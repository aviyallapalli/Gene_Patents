'''
Created on Jun 8, 2011

@author: melissafrechette
'''

from urllib2 import urlopen
import gzip
import os
from StringIO import StringIO

zippedFile = urlopen('http://www.patentlens.net/sequence/US_A/nt-inClaims.fsa.gz')


print("got this far")



file = gzip.GzipFile(fileobj=zippedFile.read())

#file = gzip.open("/Users/melissafrechette/Downloads/nt-inClaims.fsa.gz", "rb")
print("opened")

output = open("/m/canvas1/mfrechet/nt-inClaims.fsa", 'w')
output.write(str(file.read()))
output.close()

print("finished")
    
