# coding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        result = open("result.html", 'w', encoding='utf-8')
        result.write("<html>")
        result.write("<meta charset=utf-8>")
        result.write("<body>")
        result.write("<table>")
        for data in self.datas:
            result.write("<tr style='text-align:center;border:1px solid brown;'>")
            result.write("<td style='text-align:center;border:1px solid brown;'>%s</td>" % data['url'])
            result.write("<td style='text-align:center;border:1px solid brown;'>%s</td>" % data['title'])
            result.write("<td style='text-align:center;border:1px solid brown;'>%s</td>" % data['summary'])
            result.write("</tr>")

        result.write("</table>")
        result.write("</body>")
        result.write("</html>")
        result.close()
