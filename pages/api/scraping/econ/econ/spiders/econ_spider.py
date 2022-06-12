import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

econ_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://pisa.ucsc.edu',
    'Accept-Language': 'en-us',
    'Host': 'pisa.ucsc.edu',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Referer': 'https://pisa.usc.edu/class_search/',
    'Accept-Encoding': ['gzip', 'deflate', 'br'],
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'action': 'results',
    'binds[:term]': '2228',
    'binds[:reg_status]': 'all',
    'binds[:subject]': 'ECON',
    'binds[:catalog_nbr_op]': '=',
    'binds[:catalog_nbr]': '',
    'binds[:title]': '',
    'binds[:instr_name_op]': '=',
    'binds[:instructor]': '',
    'binds[:ge]': '',
    'binds[:crse_units_op]': '=',
    'binds[:crse_units_from]': '',
    'binds[:crse_units_to]': '',
    'binds[:crse_units_exact]': '',
    'binds[:days]': '',
    'binds[:times]': '',
    'binds[:acad_career]': '',
    'binds[:asynch]': 'A',
    'binds[:hybrid]': 'H',
    'binds[:synch]': 'S',
    'binds[:person]': 'P',
}

page_2_form_data_additions = {'rec_start' : '0', 'rec_dur' : '25'}

def professor_filter(item):
    return (re.search(r'\w\.', item) or "Staff" in item)

last_class_number = 0

classDict = {}

class ClassSpider(CrawlSpider):
    
    name = "classes"

    allowed_domains = ['pisa.ucsc.edu']

    start_urls = ['https://pisa.ucsc.edu/class_search/index.php']

    def start_requests(self):
        urls = ['https://pisa.ucsc.edu/class_search/index.php']

        for url in urls:
            
            yield scrapy.FormRequest(url,
                                 headers=econ_headers,
                                 formdata=data,
                                 callback=self.parse)

    
    def iterate_through_response_rows(self, response):
        all_rows = response.xpath('//div[contains(@id, "rowpanel_")]')

        for row in all_rows:
            classname = row.xpath('.//h2//a/text()').re(r'(?i)(\w+\s\w+)+\s-\s\w+\xa0+([\w\s]+\b)')
            professor = row.xpath('(.//div[@class="panel-body"]//div)[3]/text()').get().strip()
            class_number = row.xpath('(.//div[@class="panel-body"]//div)[2]/a/text()').get().strip()
            time = row.xpath('(.//div[@class="panel-body"]//div[@class="col-xs-6 col-sm-6"])[2]/text()').get().strip()
            location = row.xpath('(.//div[@class="panel-body"]//div[@class="col-xs-6 col-sm-6"])[1]/text()').get().strip()
            online_or_in_person = row.xpath('(.//div[@class="panel-body"]//div[@class="col-xs-6 col-sm-3 hide-print"])[3]/b/text()').get().strip()
            classDict[tuple(classname)] = {'professor': professor, 'class_number': class_number, 'time': time, 'location': location , 'online_or_in_person': online_or_in_person}


    def parse(self, response):

        #page = response.url.split("/")[-2]

        def request_page_2():
            page_2_form_data = data.copy().update(page_2_form_data_additions)
            yield scrapy.Request(url='https://pisa.ucsc.edu/class_search/index.php', method="POST", headers=econ_headers, body ='action=next&binds%5B%3Aterm%5D=2228&binds%5B%3Areg_status%5D=all&binds%5B%3Asubject%5D=ECON&binds%5B%3Acatalog_nbr_op%5D=%3D&binds%5B%3Acatalog_nbr%5D=&binds%5B%3Atitle%5D=&binds%5B%3Ainstr_name_op%5D=%3D&binds%5B%3Ainstructor%5D=&binds%5B%3Age%5D=&binds%5B%3Acrse_units_op%5D=%3D&binds%5B%3Acrse_units_from%5D=&binds%5B%3Acrse_units_to%5D=&binds%5B%3Acrse_units_exact%5D=&binds%5B%3Adays%5D=&binds%5B%3Atimes%5D=&binds%5B%3Aacad_career%5D=&binds%5B%3Aasynch%5D=A&binds%5B%3Ahybrid%5D=H&binds%5B%3Asynch%5D=S&binds%5B%3Aperson%5D=P&binds%5B%3Asession_code%5D=&rec_start=0&rec_dur=25')

        
        all_rows = response.xpath('//div[contains(@id, "rowpanel_")]')

        rules = (
             Rule(LinkExtractor(allow=('index/php',)), callback='parse'),
        )
        
        print(rules)
        
        for row in all_rows:
            classname = row.xpath('.//h2//a/text()').re(r'(?i)(\w+\s\w+)+\s-\s\w+\xa0+([\w\s]+\b)')
            professor = row.xpath('(.//div[@class="panel-body"]//div)[3]/text()').get().strip()
            class_number = row.xpath('(.//div[@class="panel-body"]//div)[2]/a/text()').get().strip()
            time = row.xpath('(.//div[@class="panel-body"]//div[@class="col-xs-6 col-sm-6"])[2]/text()').get().strip()
            location = row.xpath('(.//div[@class="panel-body"]//div[@class="col-xs-6 col-sm-6"])[1]/text()').get().strip()
            online_or_in_person = row.xpath('(.//div[@class="panel-body"]//div[@class="col-xs-6 col-sm-3 hide-print"])[3]/b/text()').get().strip()
            classDict[tuple(classname)] = {'professor': professor, 'class_number': class_number, 'time': time, 'location': location , 'online_or_in_person': online_or_in_person}
        
        print(classDict)

        #Finds the number at the bottom of the page and converts it to an int. Every search page displays 25 classes.
        print(response.xpath('//div[@class = "row hide-print"][last()]/b[3]/text()'))
        number_classes_available = int(response.xpath('//div[@class = "row hide-print"][last()]/b[3]/text()').get().strip())

        #If there are more than 25 classes, request the next page by adding two keywords to the original request body
        if(number_classes_available > 25):
            request_page_2()


body = 'action=next&binds%5B%3Aterm%5D=2228&binds%5B%3Areg_status%5D=all&binds%5B%3Asubject%5D=ECON&binds%5B%3Acatalog_nbr_op%5D=%3D&binds%5B%3Acatalog_nbr%5D=&binds%5B%3Atitle%5D=&binds%5B%3Ainstr_name_op%5D=%3D&binds%5B%3Ainstructor%5D=&binds%5B%3Age%5D=&binds%5B%3Acrse_units_op%5D=%3D&binds%5B%3Acrse_units_from%5D=&binds%5B%3Acrse_units_to%5D=&binds%5B%3Acrse_units_exact%5D=&binds%5B%3Adays%5D=&binds%5B%3Atimes%5D=&binds%5B%3Aacad_career%5D=&binds%5B%3Aasynch%5D=A&binds%5B%3Ahybrid%5D=H&binds%5B%3Asynch%5D=S&binds%5B%3Aperson%5D=P&binds%5B%3Asession_code%5D=&rec_start=0&rec_dur=25'