import requests


class Request(object):
    def __init__(self, req):
        self.url = req['url']
        self.get_headers(req['headers'])  # 解析请求头
        self.method = req['method']
        self.get_form(req['form'])

    def get_headers(self, req_headers):
        self.headers = {}
        headers = req_headers.split('\r\n')  # 切分每一行header

        for header in headers:
            header = header.split(':', 1)  # 切分键值
            self.headers[header[0]] = header[1].strip()  # 组成字典

    def get_form(self, req_form):
        self.form = {}

        if len(req_form) != 0:
            headers = req_form.split('\r\n')  # 切分每一行from

            for header in headers:
                header = header.split(':', 1)  # 切分键值
                self.form[header[0]] = header[1].strip()  # 组成字典

    def get(self):
        req_res = {}

        r = requests.get(self.url, headers=self.headers)
        r.encoding = "utf-8"

        # Genaral
        req_res['req_url'] = r.request.url
        req_res['status_code'] = r.status_code

        # Request
        req_res['req_headers'] = r.request.headers
        req_res['req_method'] = "GET"

        # Response
        req_res['res_headers'] = r.headers
        req_res['res_content'] = r.text

        return req_res

    def post(self):
        req_res = {}

        r = requests.post(self.url, headers=self.headers, data=self.form)
        r.encoding = "utf-8"

        # Genaral
        req_res['req_url'] = r.request.url
        req_res['status_code'] = r.status_code

        # Request
        req_res['req_headers'] = r.request.headers
        req_res['req_method'] = "POST"

        print(req_res['req_method'])

        # Response
        req_res['res_headers'] = r.headers
        req_res['res_content'] = r.text

        return req_res

    def main(self):
        if self.method == "GET":
            return self.get()
        elif self.method == "POST":
            return self.post()