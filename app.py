from model import InputForm
from flask import Flask, render_template, request
from compute import compute
from flask import Markup

app = Flask(__name__,template_folder='/Users/ssuri/test/Projects')

@app.route('/compute', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.STOCK_NAME.data)
    else:
        result = compute('AAPL')

    return render_template('view.html', form=form, result=Markup(result))

if __name__ == '__main__':
    app.run(debug=True)