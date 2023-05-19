import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def play():
if request.method == 'POST':
choices = ['rock', 'paper', 'scissors']
user_choice = request.form['choice']
computer_choice = random.choice(choices)
if user_choice == computer_choice:
result = "It's a tie!"
elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'paper' and computer_choice == 'rock' or user_choice == 'scissors' and computer_choice == 'paper':
result = "You win!"
else:
result = "Computer wins!"
return render_template('index.html', result=result)
return render_template('index.html')

if __name__ == '__main__':
app.run(debug=True)
