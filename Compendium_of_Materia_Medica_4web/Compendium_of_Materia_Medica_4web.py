 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)


@app.route('/choose_a_medica', methods=['POST'])
def pick_a_medica() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    medica_name = request.form['medica_name']	
    return render_template('results.html',
                           the_title = '请输入药名：',
                           the_medica = medica_name 
                           )
                          
 
    
    
    
    
    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到本草纲目')

if __name__ == '__main__':
    app.run(debug=True)
