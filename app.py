from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from request import Request
from flask import flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "6576"


@app.route("/", methods=['GET', 'POST'])
def index():

    # 加载页面
    if request.method == 'GET':
        return render_template("index.html")

    # 发送请求
    if request.method == 'POST':

        req = {}   # 提交表单字典

        req['url'] = request.form.get('req_url')  # 获取请求网址
        print("请求URL：", req['url'])

        req['method'] = request.form.get('req_method')  # 请求方式
        print("请求方式：", req['method'])

        req['headers'] = request.form.get('req_headers')  # 请求头
        print("请求头：", req['headers'])

        req['form'] = request.form.get('req_form')  # POST表单
        print("POST表单：", req['form'])

        if len(req['form']) == 0 and req['method'] == "POST":
            flash("POST表单为空！")

        req_res = Request(req).main()      # 请求结果

        return render_template("index.html",
                               req_url=req_res['req_url'],
                               status_code=req_res['status_code'],
                               req_method=req_res['req_method'],
                               req_headers=req_res['req_headers'].items(),
                               res_headers=req_res['res_headers'].items(),
                               res_content=req_res['res_content'],
                               )


if __name__ == '__main__':
    app.run(debug=True, port=6576)



