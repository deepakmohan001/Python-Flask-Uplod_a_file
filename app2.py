from flask import Flask,render_template,request
import os
app=Flask(__name__)
app.config['UPLOAD_PATH']='static/images'
@app.route('/')
def home():
    return render_template('eg.html')

@app.route('/upload',methods=['POST'])
def upload():
    file=request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'],file.filename))
    return 'uploaded successfully'

app.add_url_rule('/home','home',home)
if __name__=='__main__':
    app.run(debug=True)