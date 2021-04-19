class Investment:

    def __init__(self):
        pass

    def initial(self):
        print('What is the initial investment?')
        self.initial_investment = -float(input())
        return(self.initial_investment)

