#


import urllib2



def crawl_web(seed):  # returns index, graph of outlinks
    tocrawl = [seed]  # starts the crawl with one url
    crawled = []  # we haven't crawled anything yet
    graph = {}  # <url>:[list of pages it links to]
    index = {}  # <keyword>:[list of urls]
    while tocrawl:  # while there are urls left in the to crawl list
        page = tocrawl.pop()  # remove the url from the to crawl list and stores in page
        if page not in crawled:  # if we havent crawled the page yet
            content = get_real_page(page)  # returns a string containing the source code of a web page
            add_page_to_index(index, page, content)  # adds keyword:[url] pairs to the index
            outlinks = get_all_links(content)  # stores a list of all the links on the current page
            graph[page] = outlinks  # adds the current page and its outgoing links to the graph
            union(tocrawl, outlinks)  # adds all the urls on the current page to the 'to crawl' list
            crawled.append(page)  # adds the current page to the 'already crawled' list
    return index, graph


def add_page_to_index(index, url, content):  # takes in a url and its content as a string of source code
    words = content.split()  # makes a list with each word on the page as an element
    for word in words:  # for every keyword on the page
        add_to_index(index, word, url)  # adds each keyword to the index


def add_to_index(index, keyword, url):
    if keyword in index:  # if the keyword is already in the index
        index[keyword].append(url)  # add the url to the list for that keyword
    else:  # if the keyword isn't in the index
        index[keyword] = [url]  # create an entry for the keyword and url as keyword:[url]


def get_page(url):  # used to give dummy page code
    if url in cache:
        return cache[url]
    else:
        return None

def get_real_page(url):
    try:
        response = urllib2.urlopen(url)
        content = response.read()
    except:
        print 'url fail'
    return content



def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best = pages[0]
    for url in pages:
        if ranks[url] > ranks[best]:
            best = url
    return best



def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for urls in graph:
                if page in graph[urls]:
                    newrank = newrank + d * (ranks[urls] / len(graph[urls]))

            newranks[page] = newrank
        ranks = newranks
    return ranks


cache = {
    'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipes:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""",
    'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""",
    'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""",
    'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbanzo beans.
<li> Crush them in a blender.
<li> Add 3 tablespoons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
    'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
    'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""",
}

index, graph = crawl_web('https://www.udacity.com/cs101x/urank/index.html')
print index
ranks = compute_ranks(graph)

print lucky_search(index, ranks, 'try')

#if 'http://udacity.com/cs101x/urank/index.html' in graph:
 #   print graph['http://udacity.com/cs101x/urank/index.html']
# >>> ['http://udacity.com/cs101x/urank/hummus.html',
# 'http://udacity.com/cs101x/urank/arsenic.html',
# 'http://udacity.com/cs101x/urank/kathleen.html',
# 'http://udacity.com/cs101x/urank/nickel.html',
# 'http://udacity.com/cs101x/urank/zinc.html']
