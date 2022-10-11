# 01、解析和提取 HTML
# 此自动化脚本将帮助你从网页 URL 中提取 HTML，然后还为你提供可用于解析 HTML 以获取数据的功能。
# 这个很棒的脚本对于网络爬虫和那些想要解析 HTML 以获取重要数据的人来说是一种很好的享受。

def start():
    print("start : " + __name__)
    # Parse and Extract HTML
    # pip install gazpacho
    import gazpacho
    # Extract HTML from URL
    url = 'https://blog.csdn.net/qq_34035956'
    html = gazpacho.get(url)
    # print(html)

    # Extract HTML with Headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    html = gazpacho.get(url, headers=headers)
    print(html)
    # Parse HTML
    parse = gazpacho.Soup(html)
    # Find single tags
    tag1 = parse.find('h1')
    tag2 = parse.find('span')
    # Find multiple tags
    # tags1 = parse.find_all('p')
    # tags2 = parse.find_all('a')
    # Find tags by class
    tag = parse.find('.class')
    # Find tags by Attribute
    tag = parse.find("div", attrs={"class": "test"})
    # Extract text from tags
    text = parse.find('h1').text
    # text = parse.find_all('p')[0].text
