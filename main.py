import requests, re, lxml

from bs4 import BeautifulSoup

url = "https://www.promodescuentos.com/hot/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers=headers)

hot_soup = BeautifulSoup(f.content, 'lxml')

lista_hot = []
hot = hot_soup.find('div', {'class': 'cept-event-deals js-threadList listLayout-main'}).findAll('a')
# print(hoot)
num = 0
for anchor in hot:
  # print(anchor)
  urls = anchor['href']
  if re.search(r'/ofertas/', urls):
    if not re.search(r'(#comments)', urls):
      lista_hot.append(urls)
      num += 1
      hot_url = urls
      # print(hot_url)
      print('')
      hot_f = requests.get(hot_url, headers = headers)
      print(hot_f)
      hot_soup = BeautifulSoup(hot_f.content, 'lxml')
      desc = hot_soup.find('div', {'class': 'userHtml userHtml-content overflow--wrap-breakspace--h-2 space--fromW3-h-3 space--mv-3'})
      # print(hot_soup)
      print(num, urls, '\n', anchor.string.strip())
      # print('desc:' + desc.string.strip())