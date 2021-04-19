from TimeValueofMoneyFunctions import *
from Investment import *
from CashFlowSerie import *
from DictionaryManagement import *

print ( 'What do you want to do?')
user_decision = input()

function = TimeValueofMoneyFunctions()
data = DictionaryManagement()
investment = Investment()

if user_decision == 'pv':
    function.PV()

if user_decision == 'fv':
    function.FV()

if user_decision == 'npv':
    dictionary = data.create_dictionary()
    npv = investment.initial()
    data.dictionary_write(dictionary, 0, npv, npv, npv)

    cash_flow_serie = CashFlowSerie(npv)
    x = 1 
    y = cash_flow_serie.number_of_cf()
    rate = cash_flow_serie.rate_setup()

    while x <= y:
        cashflow = cash_flow_serie.create_a_cashflow(x)
        pv = cash_flow_serie.PV(cashflow, rate, x)
        npv = cash_flow_serie.NPV()
        data.dictionary_write(dictionary, x, cashflow, pv, npv)
        x +=1
    print(dictionary)
