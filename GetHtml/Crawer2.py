import requests
import bs4

def start():
    headers0 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTHL, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    }
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    }

    # result = []
    # url0 = 'https://blog.csdn.net/qq_34035956'
    # html_file0 = requests.get(url0, headers=headers0)
    # obj_soup0 = bs4.BeautifulSoup(html_file0.text, 'html.parser')
    # for link in obj_soup0.find_all('a'):  # 遍历网页中所有的超链接（a标签）
    #     value0 = "{}".format(link.get('href'))
    #     if value0.find('category_') != -1:
    #         html_file1 = requests.get(value0, headers=headers0)
    #         obj_soup1 = bs4.BeautifulSoup(html_file1.text, 'html.parser')
    #         for link1 in obj_soup1.find_all('a'):
    #             value1 = "{}".format(link1.get('href'))
    #             if value1.find('qq_34035956/article') != -1 & value1.find("comments") == -1:
    #                 result.append(value1)

    links = [
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/119854226",
        "https://blog.csdn.net/qq_34035956/article/details/100517491",
        "https://blog.csdn.net/qq_34035956/article/details/115293973",
        "https://blog.csdn.net/qq_34035956/article/details/100530182",
        "https://blog.csdn.net/qq_34035956/article/details/81176132",
        "https://blog.csdn.net/qq_34035956/article/details/100528202",
        "https://blog.csdn.net/qq_34035956/article/details/127485638",
        "https://blog.csdn.net/qq_34035956/article/details/127251755",
        "https://blog.csdn.net/qq_34035956/article/details/126033878",
        "https://blog.csdn.net/qq_34035956/article/details/117825950",
        "https://blog.csdn.net/qq_34035956/article/details/102511152",
        "https://blog.csdn.net/qq_34035956/article/details/103454014",
        "https://blog.csdn.net/qq_34035956/article/details/100517488",
        "https://blog.csdn.net/qq_34035956/article/details/100529682",
        "https://blog.csdn.net/qq_34035956/article/details/100517482",
        "https://blog.csdn.net/qq_34035956/article/details/106072568",
        "https://blog.csdn.net/qq_34035956/article/details/106156146",
        "https://blog.csdn.net/qq_34035956/article/details/106161060",
        "https://blog.csdn.net/qq_34035956/article/details/106186394",
        "https://blog.csdn.net/qq_34035956/article/details/107334475",
        "https://blog.csdn.net/qq_34035956/article/details/107368733",
        "https://blog.csdn.net/qq_34035956/article/details/108775630",
        "https://blog.csdn.net/qq_34035956/article/details/119655692",
        "https://blog.csdn.net/qq_34035956/article/details/115188374",
        "https://blog.csdn.net/qq_34035956/article/details/109255800",
        "https://blog.csdn.net/qq_34035956/article/details/80578572",
        "https://blog.csdn.net/qq_34035956/article/details/100529911",
        "https://blog.csdn.net/qq_34035956/article/details/100517492",
        "https://blog.csdn.net/qq_34035956/article/details/81632215",
        "https://blog.csdn.net/qq_34035956/article/details/100530753",
        "https://blog.csdn.net/qq_34035956/article/details/81041305",
        "https://blog.csdn.net/qq_34035956/article/details/82453782",
        "https://blog.csdn.net/qq_34035956/article/details/81978024",
        "https://blog.csdn.net/qq_34035956/article/details/80717681",
        "https://blog.csdn.net/qq_34035956/article/details/107789827",
        "https://blog.csdn.net/qq_34035956/article/details/109134111",
        "https://blog.csdn.net/qq_34035956/article/details/109558357",
        "https://blog.csdn.net/qq_34035956/article/details/110938566",
        "https://blog.csdn.net/qq_34035956/article/details/114242063",
        "https://blog.csdn.net/qq_34035956/article/details/118256003",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/100530586",
        "https://blog.csdn.net/qq_34035956/article/details/100192033",
        "https://blog.csdn.net/qq_34035956/article/details/102565387",
        "https://blog.csdn.net/qq_34035956/article/details/100530963",
        "https://blog.csdn.net/qq_34035956/article/details/100530880",
        "https://blog.csdn.net/qq_34035956/article/details/127623802",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/100915869",
        "https://blog.csdn.net/qq_34035956/article/details/127622414",
        "https://blog.csdn.net/qq_34035956/article/details/127435070",
        "https://blog.csdn.net/qq_34035956/article/details/127270127",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/126292717",
        "https://blog.csdn.net/qq_34035956/article/details/126292697",
        "https://blog.csdn.net/qq_34035956/article/details/126292677",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/104058833",
        "https://blog.csdn.net/qq_34035956/article/details/100530502",
        "https://blog.csdn.net/qq_34035956/article/details/125716963",
        "https://blog.csdn.net/qq_34035956/article/details/118370872",
        "https://blog.csdn.net/qq_34035956/article/details/114628054",
        "https://blog.csdn.net/qq_34035956/article/details/115394085",
        "https://blog.csdn.net/qq_34035956/article/details/107895244",
        "https://blog.csdn.net/qq_34035956/article/details/107829022",
        "https://blog.csdn.net/qq_34035956/article/details/106214773",
        "https://blog.csdn.net/qq_34035956/article/details/105713680",
        "https://blog.csdn.net/qq_34035956/article/details/105654647",
        "https://blog.csdn.net/qq_34035956/article/details/105631677",
        "https://blog.csdn.net/qq_34035956/article/details/105193598",
        "https://blog.csdn.net/qq_34035956/article/details/105147511",
        "https://blog.csdn.net/qq_34035956/article/details/104055922",
        "https://blog.csdn.net/qq_34035956/article/details/104053265",
        "https://blog.csdn.net/qq_34035956/article/details/104051447",
        "https://blog.csdn.net/qq_34035956/article/details/104049570",
        "https://blog.csdn.net/qq_34035956/article/details/104048005",
        "https://blog.csdn.net/qq_34035956/article/details/104036671",
        "https://blog.csdn.net/qq_34035956/article/details/104033479",
        "https://blog.csdn.net/qq_34035956/article/details/104032345",
        "https://blog.csdn.net/qq_34035956/article/details/104031950",
        "https://blog.csdn.net/qq_34035956/article/details/104031389",
        "https://blog.csdn.net/qq_34035956/article/details/104006803",
        "https://blog.csdn.net/qq_34035956/article/details/104005363",
        "https://blog.csdn.net/qq_34035956/article/details/104005075",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/125723824",
        "https://blog.csdn.net/qq_34035956/article/details/125716599",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/105736535",
        "https://blog.csdn.net/qq_34035956/article/details/100530978",
        "https://blog.csdn.net/qq_34035956/article/details/100528835",
        "https://blog.csdn.net/qq_34035956/article/details/100517500",
        "https://blog.csdn.net/qq_34035956/article/details/125509222",
        "https://blog.csdn.net/qq_34035956/article/details/81012899",
        "https://blog.csdn.net/qq_34035956/article/details/109558357",
        "https://blog.csdn.net/qq_34035956/article/details/109487482",
        "https://blog.csdn.net/qq_34035956/article/details/109255357",
        "https://blog.csdn.net/qq_34035956/article/details/100517483",
        "https://blog.csdn.net/qq_34035956/article/details/106879509",
        "https://blog.csdn.net/qq_34035956/article/details/81407373",
        "https://blog.csdn.net/qq_34035956/article/details/102924387",
        "https://blog.csdn.net/qq_34035956/article/details/81511232",
        "https://blog.csdn.net/qq_34035956/article/details/81511880",
        "https://blog.csdn.net/qq_34035956/article/details/81512100",
        "https://blog.csdn.net/qq_34035956/article/details/81512207",
        "https://blog.csdn.net/qq_34035956/article/details/81512352",
        "https://blog.csdn.net/qq_34035956/article/details/81512467",
        "https://blog.csdn.net/qq_34035956/article/details/81512854",
        "https://blog.csdn.net/qq_34035956/article/details/81513047",
        "https://blog.csdn.net/qq_34035956/article/details/81513105",
        "https://blog.csdn.net/qq_34035956/article/details/81513166",
        "https://blog.csdn.net/qq_34035956/article/details/81535678",
        "https://blog.csdn.net/qq_34035956/article/details/81777640",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/100517480",
        "https://blog.csdn.net/qq_34035956/article/details/127546041",
        "https://blog.csdn.net/qq_34035956/article/details/127515334",
        "https://blog.csdn.net/qq_34035956/article/details/127510265",
        "https://blog.csdn.net/qq_34035956/article/details/127501185",
        "https://blog.csdn.net/qq_34035956/article/details/127435286",
        "https://blog.csdn.net/qq_34035956/article/details/100517496",
        "https://blog.csdn.net/qq_34035956/article/details/125619342",
        "https://blog.csdn.net/qq_34035956/article/details/104474513",
        "https://blog.csdn.net/qq_34035956/article/details/82215784",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/106217930",
        "https://blog.csdn.net/qq_34035956/article/details/106218048",
        "https://blog.csdn.net/qq_34035956/article/details/106219357",
        "https://blog.csdn.net/qq_34035956/article/details/107921519",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/103873791",
        "https://blog.csdn.net/qq_34035956/article/details/80434830",
        "https://blog.csdn.net/qq_34035956/article/details/100529303",
        "https://blog.csdn.net/qq_34035956/article/details/100517494",
        "https://blog.csdn.net/qq_34035956/article/details/100528836",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/114630513",
        "https://blog.csdn.net/qq_34035956/article/details/100517494",
        "https://blog.csdn.net/qq_34035956/article/details/103873791",
        "https://blog.csdn.net/qq_34035956/article/details/100528836",
        "https://blog.csdn.net/qq_34035956/article/details/80434830",
        "https://blog.csdn.net/qq_34035956/article/details/104043884",
        "https://blog.csdn.net/qq_34035956/article/details/104001651",
        "https://blog.csdn.net/qq_34035956/article/details/104001321",
        "https://blog.csdn.net/qq_34035956/article/details/104000310",
        "https://blog.csdn.net/qq_34035956/article/details/103994096",
        "https://blog.csdn.net/qq_34035956/article/details/103992663",
        "https://blog.csdn.net/qq_34035956/article/details/103989777",
        "https://blog.csdn.net/qq_34035956/article/details/103972986",
        "https://blog.csdn.net/qq_34035956/article/details/103970785",
        "https://blog.csdn.net/qq_34035956/article/details/103960640",
        "https://blog.csdn.net/qq_34035956/article/details/102852530",
        "https://blog.csdn.net/qq_34035956/article/details/102617126",
        "https://blog.csdn.net/qq_34035956/article/details/102636084",
        "https://blog.csdn.net/qq_34035956/article/details/102787915",
        "https://blog.csdn.net/qq_34035956/article/details/102788075",
        "https://blog.csdn.net/qq_34035956/article/details/100527934",
        "https://blog.csdn.net/qq_34035956/article/details/82828621",
        "https://blog.csdn.net/qq_34035956/article/details/82228713",
        "https://blog.csdn.net/qq_34035956/article/details/80425343",
        "https://blog.csdn.net/qq_34035956/article/details/100517498",
        "https://blog.csdn.net/qq_34035956/article/details/100530306",
        "https://blog.csdn.net/qq_34035956/article/details/100530491",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/114635716",
        "https://blog.csdn.net/qq_34035956/article/details/114636654",
        "https://blog.csdn.net/qq_34035956/article/details/114675174",
        "https://blog.csdn.net/qq_34035956/article/details/103957350",
        "https://blog.csdn.net/qq_34035956/article/details/80425343",
        "https://blog.csdn.net/qq_34035956/article/details/80436579",
        "https://blog.csdn.net/qq_34035956/article/details/82228713",
        "https://blog.csdn.net/qq_34035956/article/details/82828621",
        "https://blog.csdn.net/qq_34035956/article/details/127785068",
        "https://blog.csdn.net/qq_34035956/article/details/127782969",
        "https://blog.csdn.net/qq_34035956/article/details/127744495",
        "https://blog.csdn.net/qq_34035956/article/details/105211280",
        "https://blog.csdn.net/qq_34035956/article/details/80723432",
        "https://blog.csdn.net/qq_34035956/article/details/80955592",
        "https://blog.csdn.net/qq_34035956/article/details/101164950",
        "https://blog.csdn.net/qq_34035956/article/details/101178528",
        "https://blog.csdn.net/qq_34035956/article/details/102127271",
        "https://blog.csdn.net/qq_34035956/article/details/102139780",
        "https://blog.csdn.net/qq_34035956/article/details/102140107",
        "https://blog.csdn.net/qq_34035956/article/details/102146294",
        "https://blog.csdn.net/qq_34035956/article/details/102155738",
        "https://blog.csdn.net/qq_34035956/article/details/102294366",
        "https://blog.csdn.net/qq_34035956/article/details/102169261",
        "https://blog.csdn.net/qq_34035956/article/details/102257343",
        "https://blog.csdn.net/qq_34035956/article/details/102333847",
    ]
    for i in range(50):
        print(i)
        for link in links:
            requests.get(link, headers=headers0)
