import scrapy
from ..items import IphonereviewItem

class iphoneReview(scrapy.Spider):
    name = 'RevScraper'
    start_urls= [
        'https://www.amazon.in/New-Apple-iPhone-12-128GB/product-reviews/B08L5TNJHG/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber='
        ]
    pageNumber = 1
    stylenumber = -1
    def parse(self,response):
        items = IphonereviewItem()
        reviewTitle = response.css('.a-text-bold span::text').extract()
        reviewText =response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "review-text-content", " " ))]//span').extract()
        styles = response.css('.a-size-mini').css('a::text').extract()
        styleName = response.css('.review-format-strip::text').extract()
        itemColour = response.css('.review-format-strip::text').extract()
        vrfFlag = response.css('.a-size-mini.a-color-state.a-text-bold::text').extract()
        rating = response.css('.review-rating .a-icon-alt::text').extract()
        # .review-rating
        items['ReviewTitle'] = reviewTitle
        items['ReviewText'] = reviewText
        items['stylenew'] = styles
        #items['StyleName'] = styles[iphoneReview.stylenumber+1] + styles[iphoneReview.stylenumber+2] + styles[iphoneReview.stylenumber+3]
        items['Colour'] = styles[0::3]
        items['StyleName'] = styles[1::3]
        items['VrfFlag'] = vrfFlag
        items['Rating'] = rating
        iphoneReview.stylenumber +=3

        yield items

        # nextpage = 'https://www.amazon.in/s?k=books&page=' + str(iphoneReview.pageNumber) + '&qid=1597588536&ref=sr_pg_2'
        # if (nextpage <= 4):
        #     yield response.follow(nextpage , callback = self.parse )
        #     iphoneReview.pageNumber += 1
        #     iphoneReview.stylenumber = -1  