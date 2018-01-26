import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoztools"
    allowed_domains = ["dmoztools.org"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)