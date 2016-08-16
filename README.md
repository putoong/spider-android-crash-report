# spider-android-crash-report

0. Beforehand
This project builds on a tutorial project from Scrapy documentation online. Scrapy is a web-scrapying engine written in Python. In this project, Scrapy version is 1.1.1, which relies on Python 2.7. It aims to go over all system crash reports (right now setup to be the first 5000 reports) in AOSP Issue Tracker (https://code.google.com/p/android/issues/list) and find reports relevant to system_server crash using keyword matching. 

1. Behavioral Description
First part is using the "spider" in the Scrapy to get all the crash reports content to a json file. The second part is to use a python script to readin the json file and do keyword matching. To execute the program, in the top most directory of the project, input:

	user@your-pc:/path-to-your-project/scrapy crawl acrash

It will take a while to finish. Some intermediate results will be printed in the console. And then, an items.jl file will be created in that folder. Then, at the same directory, input:

	user@your-pc:/path-to-your-project/python postprocessing.py

It will print all the suspicious report ids with key-word matched. The final next step is to go to the issue tracker with the id number. Examine the reports by yourself and confirm the correctness.

2. Project structure
.
├── postprocessing.py
├── README.md
├── scrapy.cfg
└── tutorial
    ├── __init__.py
    ├── items.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        ├── acrash_spider.py
        ├── __init__.py

Comments: 
	- The main data structure to keep all related information is scrapy.Item. One has to define and implement his own Item. My implementation is in items.py
	- The scrapy.Spider is the main function unit that parses the web url and scrapes data. One has to implement his own Spider. My implemenatation is in acrash_spider.py file. Understanding this file requires some knowledge (20 mins study is good enough) about XPath. Link is given below for XPath tutorial.
	- The pipeline.py is where I dump results to JSON file.

3. Tutorial and Documentation
Install Scrapy & Python: http://doc.scrapy.org/en/master/intro/install.html
Official Tutorial: http://doc.scrapy.org/en/master/intro/tutorial.html
Pipeline to JSON file: http://doc.scrapy.org/en/master/topics/item-pipeline.html
XPath Tutorial: http://www.w3schools.com/xsl/xpath_intro.asp
