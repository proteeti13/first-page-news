# print(paper.size())


# print(article_object_list[0].url)


# article_object_list[0].download()
# article_object_list[0].parse()


# # print(article_object_list[0].top_image)
# print(article_object_list[0].title)
# # print(article_object_list[0].authors)
# # print(article_object_list[0].images)
# print(article_object_list[0].top_image)
# print(article_object_list[0].publish_date)
# print(article_object_list[0].text)


# for article in article_object_list:
#     print(article.url)


import requests
from bs4 import BeautifulSoup
import articleDateExtractor
import dateparser
import newspaper
from newspaper import Article


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
url_prothom_alo = "https://www.prothomalo.com/"
url_cnn = "https://edition.cnn.com/"
url_bbc = "https://www.bbc.com/"
url_daily_star = "https://www.thedailystar.net/"
url_bdnews = "https://bdnews24.com/"
url_huffpost = "https://www.huffpost.com/"
url_nytimes = "https://www.nytimes.com/"


url_list = [
    # url_prothom_alo,
    url_cnn,
    # url_bbc,
    # url_daily_star,
    # url_bdnews,
    # url_huffpost,
    # url_nytimes,
]


for url in url_list:
    paper = newspaper.build(url, memoize_articles=False)
    article_object_list = paper.articles[0:50]
    # print(article_object_list)
    news_source_name = paper.brand
    for i in range(len(article_object_list)):
        article_url = article_object_list[i].url

        response = requests.get(article_url, headers=header)
        soup = BeautifulSoup(response.text, "lxml")
        site_name = soup.find("meta", property="og:site_name")
        title = soup.find("meta", property="og:title")
        content = soup.find("meta", property="og:description")
        url = soup.find("meta", property="og:url")
        image = soup.find("meta", property="og:image")

        article_object_list[i].download()
        article_object_list[i].parse()

        date = article_object_list[i].publish_date

        # date = dateparser.parse(soup)
        print("Source Name: ", news_source_name)
        print("For article ", i, ":")
        print(
            "site-name : ",
            site_name["content"] if site_name else "No site_name given here",
        )
        print("title : ", title["content"] if title else "No title given here")
        print(
            "content : ", content["content"] if content else "No description given here"
        )
        print("image : ", image["content"] if image else "No image given here")
        print("url : ", url["content"] if url else "No url given here")
        print("date : ", date if date else "No date given here")
        # print("date :", date)

