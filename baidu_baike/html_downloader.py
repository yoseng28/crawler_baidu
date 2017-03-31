from urllib import request


class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None
        resp = request.urlopen(url)

        if resp.getcode() != 200:
            return None
        else:
            return resp.read()
