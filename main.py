# Earning from rent calculator
from random import randrange
from flask import Flask, render_template, redirect, url_for, flash
from forms import stan
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfb7aee70e9e5cea5c8db9934e32d1a9'

@app.route('/', methods=['GET', 'POST'])



def home():
    form = stan()
    # num_1 = int(randrange(10))
    # num_2 = int(randrange(10))
    num_1 = int(5)
    num_2 = int(6)
    string = "What is " + str(num_1) + " + " + str(num_2) + "?: "

    if form.validate_on_submit:
        if form.submit.data:

            cha = num_1
            ka = num_2
            rent = form.amount.data
            rent = rent.replace(",","")
            rent = float(rent)
            duration = int(form.duration.data)
            # answ = int(form.captcha.data)
            answ = 11
            interest = str(form.interest.data)
            interest = "." + interest
            interest = float(interest)
            if answ == cha + ka:
                first_year = rent*11
                dur = duration -1
                gg = 0
                for i in range(dur):
                    intrr = rent*interest
                    rent = rent + intrr
                    total_m = rent * 11
                    gg = gg + total_m
                total_net = gg + first_year
                total_net = int(total_net)
                # total_com = '{:20,.2f}'.format(total_net)
                # total_com = total_com.strip()
                kaak = duration*11
                flash(f'Total Amount earned after {duration}  years({kaak} months) is {total_net}.', 'success')
                return redirect(url_for('home'))
                num_1 = randrange(1,10)
                num_2 = randrange(10)
            else:
                flash(f'Not able to Verify', 'danger')
                return redirect(url_for('home'))
                num_1 = randrange(1,10)
                num_2 = randrange(10)
    form.process()
    return render_template("home.html", form = form, string = string)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = True)
