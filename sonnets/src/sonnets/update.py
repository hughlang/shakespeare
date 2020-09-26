# This is the script that requests all 155 sonnets from the MIT archive and saves them as html
# fragments. This pre-download is only required once, since the content is unlikely to change. There
# is currently a bug in the MIT html where the 2-space indent of of the last two lines is not done
# with non-breaking spaces. We fix that in the code here. If they fix it on their side in the
# future, this script should be run again.

import csv
import json
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

class file_tools:
    def load_html(self, roman):
        url = 'http://shakespeare.mit.edu/Poetry/sonnet.{0}.html'.format(roman)
        print(url)
        response = requests.get(url)
        return response.text
    def load_ig_mappings(self):
        results = {}
        with open("IG-index.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results['id'] = results['instagram_id']
        csvfile.close()
        return results

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

titles = {}
ig_mappings = file_tools().load_ig_mappings()

# We know there are 154 sonnets, so this is hard coded as a loop to scrape each url page, which use
# roman numerals for unknown reasons.
for x in range(1, 155):
    roman = converter().int_to_Roman(x)
    html = file_tools().load_html(roman)
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


alldata = {}
print("===================================")
for item in sorted(titles.items()) :
    print(item[0] , " ::" , item[1] )
    alldata[item[0]] = item[1]
    if ig_mappings[item[0]] is not None:
        alldata['ig_id'] = item[1]

# Serializing json
json_object = json.dumps(alldata, indent = 4)

# Writing to sample.json
with open("sonnets.json", "w") as outfile:
    outfile.write(json_object)