class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
        
    def withdraw(self, amount, description = ''):    
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True
    
    def transfer(self, amount, dest_category):
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount, 'Transfer to ' + dest_category.name)
            dest_category.deposit(amount, 'Transfer from ' + self.name)
            return True
        
    def get_balance(self):
        trans_list=[]
        for i in range(len(self.ledger)):
            trans_list.append(self.ledger[i]["amount"])
        return sum(trans_list)
    
    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})

    def __str__(self):
        line1 = ((30-len(self.name)) // 2)*'*' + self.name + ((30-len(self.name)) // 2)*'*' + '\n'
        last_line = 'Total: ' + str("{0:.2f}".format(self.get_balance()))
        trans_str = ''
    
        for i in range(len(self.ledger)):
            ledger_2dec = "{0:.2f}".format(self.ledger[i]["amount"])
            spaces = 30 - len(self.ledger[i]["description"][0:23]) - len(ledger_2dec)
            trans_str = trans_str + self.ledger[i]["description"][0:23] + (' ' * spaces) + ledger_2dec + '\n'
        ledger_visual = line1 + trans_str + last_line
        return ledger_visual
    

def create_spend_chart(categories):
    import math
    spend_dict = []
    cat_names = []
    
    for n,cat in enumerate(categories):
        spend_dict.append(0)
        cat_names.append(cat.name)
        for i in range(len(cat.ledger)):
            if cat.ledger[i]['amount'] < 0 and 'Transfer' not in cat.ledger[i]['description']:
                spend_dict[n] += cat.ledger[i]['amount']
     
    total_spending = sum(spend_dict)
    spend_dict = [balance / total_spending for balance in spend_dict]
    spend_dict = [math.floor(balance * 10) for balance in spend_dict]
    
    chart_lines = ''
    for i in range(11):
        if i == 0:
            chart_lines += str(100-i*10) + '|'
            for balance in spend_dict:
                if 10-i <= balance:
                    chart_lines += ' o '
                else:
                    chart_lines += '   '
            chart_lines += ' \n'
        elif i == 10:
            chart_lines += '  ' + str(100-i*10) + '|'
            for balance in spend_dict:
                if 10-i <= balance:
                    chart_lines += ' o '
                else:
                    chart_lines += '   '
            chart_lines += ' \n'
        else:
            chart_lines += ' ' + str(100-i*10) + '|'
            for balance in spend_dict:
                if 10-i <= balance:
                    chart_lines += ' o '
                else:
                    chart_lines += '   '
            chart_lines += ' \n'

    seperator = '    ' + '---' * len(categories) + '-\n'
    chart_title = 'Percentage spent by category\n'
    category_titles = '    '
    longest_title = len(max(cat_names, key = len))
    
    for n,names in enumerate(cat_names):
        cat_names[n] = names.ljust(longest_title, ' ')
    
    for i in range(longest_title):
        for n in range(len(cat_names)):
            if n == (len(cat_names)-1) and not i == longest_title-1:
                category_titles += ' ' + cat_names[n][i] + '  \n    '
            elif n == (len(cat_names)-1) and i == longest_title-1:
                category_titles += ' ' + cat_names[n][i] + '  '
            else:
                category_titles += ' ' + cat_names[n][i] + ' '
    
    return chart_title + chart_lines + seperator + category_titles
    
