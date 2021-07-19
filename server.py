from flask import Flask, render_template, request, redirect
from order import Order

app = Flask(__name__)
app.secret_key = 'luv 2 connect 2 database'

@app.route('/')
def index():
    orders = Order.get_all_orders()
    return render_template('index.html', orders = orders)

@app.route('/orders/create', methods=['POST'])
def create_order():
    Order.create_order(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)