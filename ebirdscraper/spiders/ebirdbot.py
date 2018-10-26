# -*- coding: utf-8 -*-
import scrapy


class EbirdbotSpider(scrapy.Spider):
    name = 'ebirdbot'
    allowed_domains = ['www.ebird.org']

    def __init__(self,url=None, *args, **kwargs):
        super(EbirdbotSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['%s' % url]
        print('Start_URLs set as :',self.start_urls)
    '''
    start_urls = [
            'https://ebird.org/hotspot/L3612364?yr=all&m=&rank=mrec',
            ]
    '''
    '''
    start_urls = [
            'https://ebird.org/hotspot/L3612364?yr=all&m=&rank=mrec',
            'https://ebird.org/india/hotspot/L4024478?yr=all&m=&rank=mrec',
            ]
    '''
        
    def parse(self, response):
        #print(">>>>>>>>>>>>>>!!!!!!!>>>>>OUTPUT FILENAME: %s" % self.settings.attributes['FEED_URI'])
        #print(">>>>>>>>>>>>>>!!!!!!!>>>>>OUTPUT FILENAME: %s" % self.settings.get('FEED_URI'))
        #print(">>>>>>>>>>>>>>!!!!!!!>>>>>OUTPUT FILENAME: %s" % self.settings.set('FEED_URI','new_output.csv'))
        
        
       #Extract all the text corresponding to CSS class 'hotspot--name' and 'species-name' in the Hotspot page in ebird
        #hotspot_name = response.css('.hotspot--name::text').extract()     
        #species_names = response.css('.species-name::text').extract()
        #Changed the logic as there were structural changes in ebird html
        species_selector = '.species-name'
        
        for item in response.css(species_selector):
            species_name = 'a ::text'
            yield {
                'species': item.css(species_name).extract(),
                }

    '''
        #Below was the logic originally for extracting the species name from ebird scraping
        for item in species_names:
        #    print('Read item is : ',item)
            scraped_info={'species' : item}
            yield scraped_info
    '''     
    '''
    #Below is the code that I had written when trying to hardcode the multiple URLs and then extract.
    def start_requests(self):
        list_of_urls = [
                'https://ebird.org/india/hotspot/L4024478?yr=all&m=&rank=mrec',
   #             'https://ebird.org/hotspot/L3612364?yr=all&m=&rank=mrec',
                ]
        for target_url in list_of_urls:
            print('Scraping URL : ',target_url)
            yield scrapy.Request(url=target_url,callback=self.parse)
            
    def parse(self, response):
        #Extract all the text corresponding to CSS class 'species-name' in the Hotspot page in ebird
        species_names = response.css('.species-name::text').extract()

        for item in species_names:
        #    print('Read item is : ',item)
            scraped_info={'species' : item}
            yield scraped_info
    '''        
        