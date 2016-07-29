import scrapy

class AcrashSpider(scrapy.Spider):
	name = "acrash"
	allow_domains = ["dmoz.org"]
	start_urls = [
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
		"http://www.dmoz.org/Computers/Programming/Languages/Python/",
	]

	# def parse(self, response):
	# 	filename = response.url.split("/")[-2] + '.html'
	# 	with open(filename, 'wb') as f:
	# 		f.write(response.body)

	# def parse(self, response):
	# 	for sel in response.xpath('//ul/li'):
	# 		title = sel.xpath('a/text()').extract()
	# 		link = sel.xpath('a/@href').extract()
	# 		desc = sel.xpath('text()').extract()
	# 		print title, link, desc

	def parse(self, response):
		for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		for sel in response.xpath('//ul/li'):
			item = TutorialItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item

