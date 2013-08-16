from flask import Flask, render_template, request
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = #removed from public version

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = #removed from public version
app.config['MAIL_PASSWORD'] = #removed from public version

mail.init_app(app)


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if not form.validate():
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender="jake@mrbaskin.com", recipients=['jake.baskin@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/teaching')
def teaching():
  return render_template('teaching.html')
@app.route('/compsci')
def compsci():
  return render_template('compsci.html')


if __name__ == '__main__':
  app.run(debug=True)
