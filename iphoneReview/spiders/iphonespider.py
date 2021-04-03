import scrapy
from ..items import IphonereviewItem

class iphoneReview(scrapy.Spider):
    name = 'RevScraper'
    start_urls= [
        'https://www.amazon.in/New-Apple-iPhone-12-128GB/product-reviews/B08L5TNJHG/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber='
        ]
    pageNumber = 21
    def parse(self,response):
        items = IphonereviewItem()
        reviewTitle = response.css('.a-text-bold span::text').extract()
        reviewText =response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "review-text-content", " " ))]//span').extract()
        styles = response.css('.a-size-mini').css('a::text').extract()
        #styleName = response.css('.review-format-strip::text').extract()
        #itemColour = response.css('.review-format-strip::text').extract()
        vrfFlag = response.css('.a-size-mini.a-color-state.a-text-bold::text').extract()
        rating = response.css('.review-rating .a-icon-alt::text').extract()
        # .review-rating
        items['ReviewTitle'] = reviewTitle #Extracting Titles and putting them in a list
        items['ReviewText'] = reviewText #Extracting Text and putting them in a list
        items['stylenew'] = styles #Extracting Style and putting them in a list
        items['Colour'] = styles[0::3] #Extracting Color and putting them in a list
        items['StyleName'] = styles[1::3] #Extracting Style Name  and putting them in a list
        items['VrfFlag'] = vrfFlag #Extracting verified user and putting them in a list
        items['Rating'] = rating #Extracting Raiting  and putting them in a list
        

        yield items

        nextpage = 'https://www.amazon.in/New-Apple-iPhone-12-128GB/product-reviews/B08L5TNJHG/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(iphoneReview.pageNumber)
        if (iphoneReview.pageNumber <= 20):
            yield response.follow(nextpage , callback = self.parse )
            iphoneReview.pageNumber += 1