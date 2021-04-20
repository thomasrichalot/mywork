
class Calculations:

    def __init__(self, period):
        self.period = period

    def get_rate(self, present_value, future_value):
        rate = round(((future_value / present_value)**(1/self.period))-1, 4)*100
        return(rate)
    
    def pv(self, future_value, rate):
        present_value = round((future_value/(1+rate)**self.period), 2)
        return(present_value)

    def fv(self, investment, rate):
        future_value = round((investment*(1+rate)**self.period), 2)
        return(future_value)
    
    def npv(self, net_present_value, present_value):
        net_present_value += round(present_value, 2)
        return(net_present_value)



    # # # def time_value_of_money(self, function):

    # # #     if function == 'pv':
    # # #         print('What is the future value of the investment?')
    # # #         self.investment = int(input())
    # # #         print( 'In how many years?' )
    # # #         self.period = int(input())
    # # #         print( 'At what rate?' )
    # # #         self.rate = float(input())  
    # # #         self.present_value = round((self.investment/(1+self.rate)**self.period), 2)
    # # #         print ('The present value is ' + '$ '+ str(self.present_value))
    # # #         return(self.present_value)

    # # #     if function == 'fv':
    # # #         print('What is the value of the investment?')
    # # #         self.investment = float(input())
    # # #         print( 'For how many years?' )
    # # #         self.period = int(input())
    # # #         print( 'At what rate?' )
    # # #         self.rate = float(input())  
    # # #         self.future_value = round((self.investment*(1+self.rate)**self.period), 2)
    # # #         print ('The future value is ' + '$ '+ str(self.future_value))
    # # #         return(self.future_value)
        
    # # #     if function == 'rate':
    # # #         print('What is the present value?')
    # # #         self.present_value = int(input())
    # # #         print('What is the future value?')
    # # #         self.future_value = int(input())
    # # #         print('For How long?')
    # # #         self.period = int(input())
    # # #         self.rate = round(((self.future_value / self.present_value)**(1/self.period))-1, 4)
    # # #         print('The required return is ' + str(self.rate*100) + '%')
    # # #         return(self.rate)  



    # # def FV(self):
    # #     print('What is the value of the investment?')
    # #     self.investment = float(input())
    # #     print( 'For how many years?' )
    # #     self.period = int(input())
    # #     print( 'At what rate?' )
    # #     self.rate = float(input())  
    # #     self.future_value = round((self.investment*(1+self.rate)**self.period), 2)
    # #     print ('The future value is ' + '$ '+ str(self.future_value))
    # #     return(self.future_value)

    # # def PV(self):
    # #     print('What is the future value of the investment?')
    # #     self.investment = int(input())
    # #     print( 'In how many years?' )
    # #     self.period = int(input())
    # #     print( 'At what rate?' )
    # #     self.rate = float(input())  
    # #     self.present_value = round((self.investment/(1+self.rate)**self.period), 2)
    # #     print ('The present value is ' + '$ '+ str(self.present_value))
    # #     return(self.present_value)

    # # def rate_of_return(self):
    # #     print('What is the present value?')
    # #     self.present_value = int(input())
    # #     print('What is the future value?')
    # #     self.future_value = int(input())
    # #     print('For How long?')
    # #     self.period = int(input())
    # #     self.rate = round(((self.future_value / self.present_value)**(1/self.period))-1, 4)
    # #     print('The required return is ' + str(self.rate*100) + '%')
    # #     return(self.rate)