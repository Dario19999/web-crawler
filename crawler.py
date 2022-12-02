import threading, re
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Worker:
    base_url = ''
    lista = []
    crawled = set()
    lock = threading.Semaphore(value=1)

    def __init__(self, base_url):
        self.base_url = base_url
        self.lista = [base_url]

    @staticmethod
    def write_file(path, data):
        with open(path, 'a') as f:
            f.write(data)
            f.close()

    def report(self, url):
        with self.lock:
              print("Crawled", url)

    def work(self):
        for link in self.lista:

            try:
                page = urlopen(link)
                soup = BeautifulSoup(page, 'lxml')

                self.write_file("contenido.txt", soup.text)
                if re.search(r'/ofertas/', link):
                  if not re.search(r'(#comments)', link):
                    self.write_file("ofertas.txt", link + "\n")
                self.report(link)
                self.crawled.add(link)

                for upper_domain in soup.find_all('a', href=True):
                    joined_link = urljoin(self.base_url, upper_domain['href'])
                    if joined_link not in self.crawled:
                        self.lista.append(joined_link)
            except:
                #links con error se van al log de error
                self.write_file("error.txt", str(link) + "\n")
                pass

