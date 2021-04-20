

from Calculations import *
from ConsoleManagement import *
from DictionaryManagement import *


data = DictionaryManagement()
console = ConsoleManagement()

console.display_text('What do you want to do?')
user_decision = console.get_input()

def calculate_pv():
    console.display_text('What is the future value of the investment?')
    future_value = float(console.get_input())
    console.display_text('In how many years?')
    period = int(console.get_input())
    console.display_text('What is the discount rate?')
    rate = float(console.get_input())
    calculation = Calculations(period)
    present_value = calculation.pv(future_value, rate)
    console.display_text('The present value is $' + str(present_value))

def calculate_fv():
    console.display_text('What is the value of the investment?')
    investment = float(console.get_input())
    console.display_text('For how many years?')
    period = int(console.get_input())
    console.display_text('What is the discount rate?')
    rate = float(console.get_input())
    calculation = Calculations(period)
    future_value = calculation.fv(investment, rate)
    console.display_text('The future value is $' + str(future_value))

def calculate_rate():
    console.display_text('What is the value of the investment?')
    present_value = float(console.get_input())
    console.display_text('What is the future value of the investment?')
    future_value = float(console.get_input())
    console.display_text('For how many years?')
    period = int(console.get_input())
    calculation = Calculations(period)
    rate = calculation.get_rate(present_value, future_value)
    console.display_text('The rate is ' + str(rate) + '%') 

def calculate_npv():
    dictionary = data.create_dictionary()
    
    console.display_text('What is the initial investment?')
    investment = float(console.get_input())
    net_present_value = -investment
    data.dictionary_write(dictionary, 0, investment, investment, investment)


    console.display_text('How many Cashflows do you have?')
    y = int(console.get_input())
    x = 1 
    calculation = Calculations(x)

    console.display_text('What is the interest rate used?')
    rate = float(console.get_input())

    while x <= y:
        console.display_text("What is cashflow number " + str(x))
        cashflow = float(console.get_input())
        present_value = calculation.pv(cashflow, rate)
        net_present_value = calculation.npv(net_present_value, present_value)
        data.dictionary_write(dictionary, x, cashflow, present_value, net_present_value)
        x +=1
    print(dictionary)
    

def error():
    console.display_text('Error: this function is not regognized')
    console.display_text('List of supported functions:')
    console.display_text('Present value = p; Future value = fv; Rate = rate; Net present value = npv')


if user_decision == 'pv':
    calculate_pv()

if user_decision == 'fv':
    calculate_fv()

if user_decision == 'rate':
    calculate_rate()
  
if user_decision == 'npv':
    calculate_npv()

else:
    error()