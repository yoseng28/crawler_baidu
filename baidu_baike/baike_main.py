# coding:utf8
from baidu_baike import html_downloader
from baidu_baike import html_outputer
from baidu_baike import url_manager
from baidu_baike import html_parser


class BaikeMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("正在爬取第 %d 页面：%s" % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count += 1
            except:
                print("爬取页面失败！")

        print("\n页面爬取结束！")
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    baike_main = BaikeMain()
    baike_main.craw(root_url)
