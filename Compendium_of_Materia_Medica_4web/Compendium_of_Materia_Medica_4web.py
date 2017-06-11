 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)


@app.route('/choose_a_plant', methods=['POST'])
def pick_a_flower() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    plant_name = request.form['plant_name']	
    return render_template('results.html',
                           the_title = '请输入植物名：',
                           the_plant = plant_name 
                           )
                          
 
    
    
    
    
    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到植物世界')

if __name__ == '__main__':
    app.run(debug=True)
