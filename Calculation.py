from Operations import Operations

class Calculation():
    def __init__(self):
        self.self = self


    def calculation(self, expression):
        char1 = 'char1'
        char2 = 'char2'
        symbol = 'symbol'
        parser = {char1: [], symbol: [], char2: []}

        for char in expression:
            if char == '-':
                expression.replace('-', '(-')
            pass

        for char in expression:
            if expression[0] == '-':
                continue
            if not char.isdigit():
                parser[symbol].append(char)
                x = expression.split(char, 1)
                parser[char1].append(x[0])
                parser[char2].append(x[1])

        a = int(parser[char1][0])
        b = int(parser[char2][0])
        op = Operations(a, b)
        total = 0
        if parser[symbol][0] == '+':
            total = op.addition(a, b)
        elif parser[symbol][0] == '-':
            total = op.difference(a, b)
        elif parser[symbol][0] == '*':
            total = op.product(a, b)
        elif parser[symbol][0] == '/':
            total = op.quotient(a, b)
        print(total)

        off_switch = ''
        while off_switch != '~':
            expression = input()
            if expression == '~':
                break

            char1 = total
            char2 = 'char2'
            symbol = 'symbol'
            parser = {char1: [total], symbol: [], char2: []}

            for char in expression:
                if not char.isdigit():
                    parser[symbol].append(char)
                    x = expression.split(char)
                    parser[char2].append(x[1])
                    break

            a = int(parser[char1][0])
            b = int(parser[char2][0])
            op = Operations(a, b)

            off_switch = ''
            if parser[symbol][0] == '+':
                total = op.addition(a, b)
            elif parser[symbol][0] == '-':
                total = op.difference(a, b)
            elif parser[symbol][0] == '*':
                total = op.product(a, b)
            elif parser[symbol][0] == '/':
                total = op.quotient(a, b)
            print(total)
    pass