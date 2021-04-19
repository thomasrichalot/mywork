class CashFlowSerie:

    def __init__(self, npv):
        self.npv = npv
        pass

    def dictionary_init(self):
        self.dictionary = {
        "Year":[],
        "Cash Flow": [],
        "Present Value": [],
        "Net Present Value": []
        }
        return(self.dictionary)

    def dictionary_write(self, dictionary, nper, cashflow, pv, npv):
        self.dictionary['Year'].append(nper)
        self.dictionary['Cash Flow'].append(cashflow)
        self.dictionary['Present Value'].append(pv)
        self.dictionary['Net Present Value'].append(round(self.npv, 2))


    def number_of_cf(self):
        print('How many cash flows do you have?')
        self.number_of_cashflows = int(input())
        return(self.number_of_cashflows)
    
    def rate_setup(self):
        print('What is the discount rate used?')
        self.rate = float(input())
        return(self.rate)

    def create_a_cashflow(self, nper):
        self.nper = nper
        print('What is the amount of Cash Flow numero' + str(self.nper) + '?')
        self.amount = float(input())
        return(self.amount)
        
    def PV(self, amount, rate, nper):
        self.present_value = round((amount/(1+rate)**nper),2)
        print('The present value of the cash flow is $' + str(self.present_value))
        return(self.present_value)
    
    def NPV(self):
        self.npv += round(self.present_value, 2)
        print('The net present value of the cash flow is $' + str(round(self.npv, 2)))
        return(self.npv)
