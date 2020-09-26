# This is the script that requests all 155 sonnets from the MIT archive and saves them as html
# fragments. This pre-download is only required once, since the content is unlikely to change. There
# is currently a bug in the MIT html where the 2-space indent of of the last two lines is not done
# with non-breaking spaces. We fix that in the code here. If they fix it on their side in the
# future, this script should be run again.

import re
import requests
from bs4 import BeautifulSoup

class converter:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

class page_builder:
    def scraper(self, roman):
        url = 'http://shakespeare.mit.edu/Poetry/sonnet.{0}.html'.format(roman)
        print(url)
        response = requests.get(url)
        return response.text


titles = {}

# We know there are 154 sonnets, so this is hard coded as a loop to scrape each url page, which use
# roman numerals for unknown reasons.
for x in range(1, 155):
    roman = converter().int_to_Roman(x)
    html = page_builder().scraper(roman)
    soup = BeautifulSoup(html, 'html.parser')
    quote = str(soup.body.blockquote)
    quote = re.sub(u'  ', '&nbsp;&nbsp;', quote)
    line1 = soup.body.blockquote.contents[0]
    line1 = line1.rstrip(',;:')
    titles[x] = line1
    path = './fragments/poem-{0}.htm'.format(x)
    file = open(path, 'w')
    file.write(quote)
    file.close()


print("===================================")
for item in sorted(titles.items()) :
    print(item[0] , " ::" , item[1] )

