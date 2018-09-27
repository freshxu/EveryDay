#!/usr/bin/python
#coding=utf-8
import json
import urllib2
import os
import subprocess
import datetime
import codecs
def get_iciba():
	url = 'http://open.iciba.com/dsapi/'
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	json_data = response.read()
	data = json.loads(json_data)
	return data

def getContent():
	return get_iciba()['content']

def getNote():
	return get_iciba()['note']

def pushgit():
	os.chdir("/root/freshxu/EveryDay")
	day = datetime.datetime.now().strftime("%Y-%m-%d")
	fp = codecs.open('README.md','a+','utf-8')
	content = getContent()
	note = getNote()
	fp.write("### " + day +"  \n" + content + "  \n" + note + "  \n")
	fp.close()
	try:
        	subprocess.call(["git", "add", "."])
        	subprocess.call(["git", "commit", "-m",day + "又特娘的是元气满满的一天哦！"])
        	subprocess.call(["git", "push"])
	except Exception as e:
        	print(e)

pushgit()
