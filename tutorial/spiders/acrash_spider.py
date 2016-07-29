import scrapy
from tutorial.items import AcrashItem

class AcrashSpider(scrapy.Spider):

	name = "acrash"
	allow_domains = ["code.google.com"]
	start_urls = [
		"https://code.google.com/p/android/issues/list?can=1&q=crash&sort=-opened&colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&cells=tiles"
	]

	def parse(self, response):
		for sel in response.xpath('//td[@class="vt id col_0"]'):
			link = sel.xpath('a/@href').extract()
			url = response.urljoin(link[0]);
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = AcrashItem()
		item['id'] = response.xpath('//td[@class="vt h3"]/a/text()').extract()
		item['title'] = response.xpath('//title/text()').extract()
		item['link'] = response.url;
		# item['text'] = response.xpath('//pre/text()').extract()
		yield item
