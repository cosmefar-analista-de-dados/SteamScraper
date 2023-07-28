from selectolax.parser import HTMLParser
from utils.extract import extract_full_body_html

URL = "https://store.steampowered.com/specials"

if __name__ == '__main__':

    html = extract_full_body_html(
        from_url = URL,
        wait_for = 'div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]')

    tree = HTMLParser(html)
    # this means contains
    divs = tree.css('div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]')

    for div in divs:
        title = div.css_first('a div[class*="StoreSaleWidgetTitle"]').text()
        thumbnail = div.css_first('img[class*="CapsuleImage"]').attributes.get("src")
        tags = [a.text() for a in div.css('div[class*="StoreSaleWidgetTags"] > a')[:5]]
        release_date = div.css_first(
            'div[class*="WidgetReleaseDateAndPlatformCtn"] > div[class*="StoreSaleWidgetRelease"]'
        ).text()
        review_count = div.css_first('div[class*="ReviewScoreCount"]').text()
        review_score = div.css_first('div[class*="ReviewScoreValue"] > div').text()
        sale_price = div.css_first('div[class*="StoreSalePriceBox"]').text()
        original_price = div.css_first('div[class*="StoreOriginalPrice"]').text()

        data = {

            'title': title,
            'tags': tags,
            'review_count': review_count,
            'review_score': review_score,
            'release_date': release_date,
            'sale_price': sale_price,
            'original_price': original_price,
            'thumbnail': thumbnail

        }

        print(data)
