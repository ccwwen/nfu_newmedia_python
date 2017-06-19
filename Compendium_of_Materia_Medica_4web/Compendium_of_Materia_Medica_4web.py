 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from pick_medica_value import medica_value

app = Flask(__name__)


@app.route('/pick_a_medica', methods=['POST'])
def pick_a_medica() -> 'html':
    try:
        medica_name = request.form['medica_name']
        list_medica = medica_value(medica_name)
        return render_template('results.html',
                               the_title = '以下是输出结果',
                               output_value_释名 = list_medica[0],
                               output_value_气味 = list_medica[1],
                               output_value_主治 = list_medica[2]
                               )
    except:
        return render_template('entry.html',
                           the_output_prompt='输入错误',
                           the_title='欢迎来到本草纲目')
                          
 
    
    
    
    
    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
   output_prompt = '请输入你想要搜索的药名'
    return render_template('entry.html',
                           the_output_prompt=output_prompt,
                           the_title='欢迎来到本草纲目')
  
if __name__ == '__main__':
    app.run(debug=True)
