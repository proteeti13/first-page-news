import requests
from bs4 import BeautifulSoup
import articleDateExtractor
import dateparser


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
url_prothom_alo = "https://www.prothomalo.com/bangladesh/article/1614818/%E2%80%98%E0%A6%AA%E0%A6%9B%E0%A6%A8%E0%A7%8D%E0%A6%A6%E0%A7%87%E0%A6%B0%E2%80%99-%E0%A6%97%E0%A6%BE%E0%A7%9C%E0%A6%BF-%E0%A6%95%E0%A6%BF%E0%A6%A8%E0%A6%A4%E0%A7%87-%E0%A7%AA%E0%A7%AE-%E0%A6%B2%E0%A6%BE%E0%A6%96-%E0%A6%9F%E0%A6%BE%E0%A6%95%E0%A6%BE-%E0%A6%AC%E0%A6%BE%E0%A7%9C%E0%A6%A4%E0%A6%BF-%E0%A6%97%E0%A7%81%E0%A6%A8%E0%A6%9B%E0%A7%87-%E0%A6%AC%E0%A6%BF%E0%A6%AE%E0%A6%BE%E0%A6%A8"
url_cnn = "https://edition.cnn.com/interactive/2019/09/business/samsung-headquarters-south-korea/index.html"
url_bbc = "https://www.bbc.com/news/av/stories-49666419/life-saving-surgery-but-not-by-a-doctor"
url_daily_star = "https://www.thedailystar.net/frontpage/rohingyas-voter-list-election-commission-staffers-fraud-ring-behind-it-1801495"
url_bdnews = "https://bdnews24.com/world/2019/09/18/iran-s-rouhani-blames-us-saudi-for-conflict-in-region"
url_huffpost = "https://www.huffpost.com/entry/migrant-mothers-children-suing-trump-asylum-ban_n_5d819313e4b0957256ada9d6?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuaHVmZnBvc3QuY29tLw&guce_referrer_sig=AQAAANOwUFQmmgtG832C2zFu5uIzShOo3_RozywzkTKf85PBdUFTHQKAGjHyBDynkdwTJxHck2dYWcFBGL2IzcnmF5qdCPWruhCVMQGJ6w0r-1adq1h7JtIyl6ebGslvov3BUdBonintC93gn1dTVOJkdSpfmxkd4L0zipjURTlwZjhC"
url_nytimes = "https://www.nytimes.com/2019/09/17/climate/trump-california-emissions-waiver.html?action=click&module=Top%20Stories&pgtype=Homepage"


url_list = [
    url_prothom_alo,
    url_cnn,
    url_bbc,
    url_daily_star,
    url_bdnews,
    url_huffpost,
    url_nytimes,
]


for url in url_list:
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "lxml")
    site_name = soup.find("meta", property="og:site_name")
    title = soup.find("meta", property="og:title")
    content = soup.find("meta", property="og:description")
    url = soup.find("meta", property="og:url")
    image = soup.find("meta", property="og:image")

    # date = dateparser.parse(soup)

    print(
        "site-name : ", site_name["content"] if site_name else "No site_name given here"
    )
    print("title : ", title["content"] if title else "No title given here")
    print("content : ", content["content"] if content else "No description given here")
    print("image : ", image["content"] if image else "No image given here")
    print("url : ", url["content"] if url else "No url given here")
    # print("date :", date)

# from newspaper import Article

# url = "https://bdnews24.com/world/2019/09/18/iran-s-rouhani-blames-us-saudi-for-conflict-in-region"
# article = Article(url)
# article.download()
# article.parse()
# print(article.publish_date)
