import scrapy
from tutorial.items import AcrashItem

class AcrashSpider(scrapy.Spider):

	depth = 0;
	base_url = "https://code.google.com/p/android/issues/"
	name = "acrash"
	allow_domains = ["code.google.com"]
	start_urls = [
		"https://code.google.com/p/android/issues/list?can=1&q=crash&sort=-opened&colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&cells=tiles"
		# "https://code.google.com/p/android/issues/list?can=1&q=crash&colspec=ID%20Status%20Priority%20Owner%20Summary%20Stars%20Reporter%20Opened&sort=-opened&num=100&start=100"
	]

	def parse(self, response):
		if self.depth >= 10:
			return

		for sel in response.xpath('//td[@class="vt id col_0"]'):
			link = sel.xpath('a/@href').extract()
			url = response.urljoin(link[0]);
			yield scrapy.Request(url, callback=self.parse_dir_contents)
		print "{PD}@parse" + str(self.depth)
		# next page and next next .. until first 1000 entries, which is 10 pages
		self.depth = self.depth + 1
		# there are two next buttons in the page while we only need one
		for next in response.xpath('//div[@class="pagination"]/a'):
			mstr =  next.xpath('text()').extract()[0]
			if str(mstr)[0] is 'N':
				nextUrl = self.base_url + next.xpath('@href').extract()[0]
				yield scrapy.Request(nextUrl, callback=self.parse)
				break;
			# theNextUrl = response.urljoin(next[0]);
			# yield scrapy.Request(theNextUrl, callback=self.parse)
			# break




	def parse_dir_contents(self, response):
		item = AcrashItem()
		item['id'] = response.xpath('//td[@class="vt h3"]/a/text()').extract()
		item['title'] = response.xpath('//title/text()').extract()
		item['link'] = response.url;
		item['text'] = response.xpath('//pre/text()').extract()
		yield item
