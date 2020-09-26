# This script is used to rebuild all pages using the `template-sonnet.html` file. This will need to
# happen whenever a design change has been made in the template. Updated files are published to the
# `www` folder. After verifying the content is correct, you can push the changes to master, which
# will publish the updated site to Netlify.

from bs4 import BeautifulSoup

class assembly:
    def build_page(self, page_id, page_num, quote):
        print('{0}  {1}'.format(page_num, page_id))


for x in range(1, 155):
    assembly().build_page('XXXX', x, 'quote')
    # roman = converter().int_to_Roman(x)
    # html = page_builder().scraper(roman)
    # soup = BeautifulSoup(html, 'html.parser')
    # quote = str(soup.body.blockquote)
    # quote = re.sub(u'  ', '&nbsp;&nbsp;', quote)
    # path = 'poem-{0}.htm'.format(x)
    # file = open(path, 'w')
    # file.write(quote)
    # file.close()
