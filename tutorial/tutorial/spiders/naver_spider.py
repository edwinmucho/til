import scrapy

class naverSpider(scrapy.Spider):
    name = "navergo"
    allowed_domains = ["m.blog.naver.com"]
    start_urls = [
        "https://m.blog.naver.com/progagmer/194973060"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)