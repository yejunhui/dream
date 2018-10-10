from indexmian import Index
from tandw import Taw
from flask import Flask,render_template,session,url_for,request,redirect,abort,make_response,send_file,send_from_directory
import os

	

app = Flask(__name__)

app.config['SECRET_KEY']=os.urandom(24)
#登录
@app.route('/',methods = ['GET','POST'])
def login():
	if request.method == 'POST' :
		session['user'] = request.form['user']
		session['password'] = request.form['password']
		return redirect(url_for('index'))
	else :
		t,w = Taw.taw()
		return render_template('login.html',w = w,time = t)

#开始
@app.route('/index',methods = ['GET','POST'])
def index():
	if Index.selectuser(user = session.get('user'),password = session.get('password')) == 1 :
		t,w = Taw.taw()
		return	render_template('index.html',w = w,time = t,session=session)
	else :
		return redirect(url_for('login'))

#主页
@app.route('/indexm')
def indexm ():
	if Index.selectuser(user = session.get('user'),password = session.get('password')) == 1 :
		t,w = Taw.taw()
		return render_template('index_mune.html',w = w,time = t)
	else :
		return redirect(url_for('login'))

#功能页
@app.route('/mune')
def mune ():
	if Index.selectuser(user = session.get('user'),password = session.get('password')) == 1 :
		t,w = Taw.taw()
		return render_template('index_mune',w = w,time = t)
	else :
		return redirect(url_for('login'))

@app.route('/data',methods=['GET','POST'])
def data ():
	if Index.selectuser(user = session.get('user'),password = session.get('password')) == 1 :
		t,w = Taw.taw()
		return render_template('data.html',w = w,time = t)
		f = request.form['files']
	else :
		return redirect(url_for('login'))

@app.route('/download')
def downloadFile(filename):
	directory = url_for('static',filename = 'dow')
	response = make_response(send_from_directory(directory,filename,as_attachment=True))
	response.headers['Content-Disposition'] = 'attachment; filename={}',format(filename.encode('utf-8').decode('utf-8'))
	return response

#帮忙页
@app.route('/help')
def help():
	t,w = Taw.taw()
	return render_template('help.html',w = w,time = t)

#退出
@app.route('/logout')
def logout():
	session.pop('user',None)
	session.pop('password',None)
	session.pop('type',None)
	return redirect(url_for('login'))

#500异常
@app.errorhandler(500)
def notfound(e):
    return redirect(url_for('login'))


#当index.py为主打开文件时启动服务器，打开调试，端口80，打开内网监听
if __name__ == '__main__' :
	app.debug=1
	app.run('0.0.0.0',80)