
class TimeValueofMoneyFunctions:

    def __init__(self):
        pass

    def FV(self):
        print('What is the value of the investment?')
        self.investment = float(input())
        print( 'For how many years?' )
        self.period = int(input())
        print( 'At what rate?' )
        self.rate = float(input())  
        self.future_value = round((self.investment*(1+self.rate)**self.period), 2)
        print ('The future value is ' + '$ '+ str(self.future_value))
        return(self.future_value)

    def PV(self):
        print('What is the future value of the investment?')
        self.investment = int(input())
        print( 'In how many years?' )
        self.period = int(input())
        print( 'At what rate?' )
        self.rate = float(input())  
        self.present_value = round((self.investment/(1+self.rate)**self.period), 2)
        print ('The present value is ' + '$ '+ str(self.present_value))
        return(self.present_value)

    def rate_of_return(self):
        print('What is the present value?')
        self.present_value = int(input())
        print('What is the future value?')
        self.future_value = int(input())
        print('For How long?')
        self.period = int(input())
        self.rate = round(((self.future_value / self.present_value)**(1/self.period))-1, 4)
        print('The required return is ' + str(self.rate*100) + '%')
        return(self.rate)