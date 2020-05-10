import urllib.request, urllib.parse, urllib.error
import os
import time
from datetime import datetime


base_url="https://covid19.geo-spatial.org/api/dashboard/"
data_list=["getCasesByCounty","getDeadCasesByCounty","getHealthCasesByCounty","getDailyCaseReport"]


def time_stamping_machine(own_function):
    def internal_wrapper(*args, **kwargs):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print()
        print(string_timestamp)
        return own_function(*args, **kwargs)
    return internal_wrapper

@time_stamping_machine
def download(links,data_list):	
	for link,fname in zip(links,data_list):
		file = urllib.request.urlopen(link)
		data_dir=os.path.join(os.path.dirname(os.getcwd()),"datasets/")  ### create datasate file path
		os.chdir(data_dir)                                               ### change to dataset file path
		
		 
		fname=fname+".json"				                
		fhand = open(fname, 'wb')
		size = 0
		time.sleep(2)
		while True:
				info = file.read(100000)
				if len(info) < 1: break
				size = size + len(info)
				fhand.write(info)

		print(size, 'characters copied to', fname)
		fhand.close()
		time.sleep(3)
links=[]
for item in data_list:
	link=urllib.parse.urljoin(base_url, item)
	links.append(link)

download(links,data_list)
