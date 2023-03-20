from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    if request.form.get('reset') == 'yes':
      with open('expenses.txt', 'w') as file:
        file.write('Example,10,10')
    description = request.form.get('description')
    if not description:
      description = 'No description'
    spent = request.form.get('spent')
    if not spent:
      spent = '0'
    added = request.form.get('added')
    if not added:
      added = '0'
    with open('expenses.txt', 'a') as file:
      file.write('\n' + description + ',' + spent + ',' + added)
  dataset = []
  with open('expenses.txt', 'r') as file:
    line = file.read()
    data = line.split('\n')
    for element in data:
      list = element.split(',')
      description = list[0]
      spent = int(list[1])
      added = int(list[2])
      dataset.append((description, spent, added))
    total_spent = sum([thing[1] for thing in dataset])
    total_added = sum([thing[2] for thing in dataset])
    total = total_added - total_spent
    if total < 0:
     with open('secret.txt', 'r') as file:
       secret = file.read()
    else:
      secret = ''
  return render_template('index.html', data=dataset, total=total, total_spent=total_spent, total_added=total_added, secret=secret)
  
app.run(host='0.0.0.0', port=81)
