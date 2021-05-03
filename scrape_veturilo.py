#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET

from datetime import datetime
import time
import csv
import unidecode
#import os

def WriteListToCSV(csv_file,data_list):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            #writer.writerow(csv_columns) #we append to the file so we don't want to add column names every time
            for data in data_list:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return

#def get_website(url):
#    return requests.get(url, allow_redirects=True)

def get_website(url):
    try:
        r = requests.get(url,timeout=3)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        return "err"
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return "err"
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return "err"
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        return "err"
    return requests.get(url, allow_redirects=True)


#def create_list(tree):
#    date = str(datetime.now())
#    l = []
#    for place in tree.iter('place'):
#        if 'bike_numbers' in place.attrib:
#            l.append([date, place.attrib['number'], unidecode.unidecode(unicode(place.attrib['name'])),place.attrib['bike_racks'],place.attrib['bike_numbers'].encode('utf-8')])
#        else:
#            l.append([date, place.attrib['number'], unidecode.unidecode(unicode(place.attrib['name'])),place.attrib['bike_racks'],"0"])
#    return l

def create_list(tree):
    date = str(datetime.now())
    l = []
    for place in tree.iter('place'):
        if 'bike_numbers' in place.attrib:
            l.append([date, int(place.attrib['number']), int(place.attrib['bike_racks']),place.attrib['bike_numbers']])
        else:
            l.append([date, int(place.attrib['number']), int(place.attrib['bike_racks']),""])
    return l

while True:
    response = get_website('http://nextbike.net/maps/nextbike-official.xml?city=210')
    if response != "err":
        tree = ET.fromstring(response.content)
        l = create_list(tree)
        WriteListToCSV('veturilo_statistics.csv',l)
    time.sleep(300)
