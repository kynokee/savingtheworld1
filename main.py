from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
  data = None
  name = None
  gender = None
  Class = None
  H2 = None
  H1 = None
  with open('intro.txt', 'r') as file:
    msg = file.read()
  if request.method == 'POST':
    name = request.form.get('name')
    Class = request.form.get('class')
    gender = request.form.get('gender')
    H2 = request.form.getlist('H2')
    H1 = request.form.get('H1')
    data = name + ' ' + Class + ' ' + gender + ' H1: ' + H1 + ' H2: ' 
    for sub in H2:
      data = data + sub + ' '
    with open('secret.txt', 'a') as file:
      file.write(data + '\n')
  return render_template('index.html', intro=msg, egg=Class)

app.run(host='0.0.0.0', port=81)
