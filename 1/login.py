from flask import Flask, render_template, jsonify,url_for,request, redirect
app = Flask(__name__)
DATA_DICT = {
    1:{'name':'罗本',"age":38},
    2:{'name':'库里',"age":34},
}
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        #return '登录'#HttpResponse
        #return render_template('login.html')#render
        #return jsonify({'code':1000,"data":[1,2,3]})#JsonReponse
        return render_template('login.html')
    user = request.form.get('user')
    password = request.form.get('password')
    if user == 'zhuyeye' and password == 'hanhan24322=':
        return redirect('/index')
    error = '用户名或者密码错误'
    return render_template('login.html', error=error)
@app.route('/index',endpoint='idx')
def index():
    data_dict = DATA_DICT
    return render_template('index.html',data_dict=DATA_DICT)
@app.route('/edit',methods=['GET','POST'])
def edit():
    nid = request.args.get('nid')
    nid = int(nid)
    if request.method == 'GET':
        info = DATA_DICT[nid]
        return render_template('edit.html',info=info)
    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    return redirect(url_for('idx'))
@app.route('/del/<int:nid>')
def delete(nid):
    del DATA_DICT[nid]
    #return redirect('/index')
    return redirect(url_for("idx"))
if __name__ == '__main__' :
    app.run()