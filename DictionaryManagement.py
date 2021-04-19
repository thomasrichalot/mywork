class DictionaryManagement:

    def __init__(self):
        pass

    def create_dictionary(self):
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
        self.dictionary['Net Present Value'].append(round(npv, 2))