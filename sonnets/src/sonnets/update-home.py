# This script updates the home page grid of thumbnail content

import copy
from bs4 import BeautifulSoup

# This code takes the toc template and finds the first grid tile which has sample data. By copying
# this tile and modifying certain attributes, it can then be appended to the DOM. Here is a copy of
# the first tile.
# <div id="tile-1" class="col-md-4 tile">
#     <a href="sonnets/sonnet-1.html">
#         <p class="tile_text">SAMPLE</p>
#     </a>
# </div>

with open("template-toc.html") as template:
    soup = BeautifulSoup(template, 'html.parser')
    tile1 = soup.find(id='tile-1')
    if tile1 is None:
        print('Did not find tile-1')

    container = tile1.parent
    for i in range(2, 155):
        newtile = copy.copy(tile1)
        new_id = 'tile-{0}'.format(i)
        newtile['id'] = new_id
        new_url = 'sonnets/sonnect-{0}'.format(i)
        newtile.a['href'] = new_url
        # container.in
        html = str(soup.prettify("utf-8"))
        outpath = '../../www/sonnets/sonnet-{0}.html'.format(i)
        with open(outpath, "w") as file:
            file.write(html)
            file.close()


