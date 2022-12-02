from crawler import *

def crawl(url):
    current_worker = Worker(url)
    load = threading.Thread(target=current_worker.work)
    load.start()

if __name__ == '__main__':
    print("Crawler para ofertas hot de promodescuentos")
    crawl('https://www.promodescuentos.com/hot/')