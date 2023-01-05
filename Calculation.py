from Operations import Operations


class Calculation:
    def __init__(self):
        self.self = self
        self.char1 = 'char1'
        self.char2 = 'char2'
        self.symbol = 'symbol'

    def calculation(self, expression):
        parser = {self.char1: [], self.symbol: [], self.char2: []}

        for char in expression:
            if expression[0] == '-':
                continue
            if not char.isdigit():
                parser[self.symbol].append(char)
                x = expression.split(char, 1)
                parser[self.char1].append(x[0])
                parser[self.char2].append(x[1])

        total = self.operation_result(parser, parser[self.symbol][0])
        print(total)

        off_switch = ''
        while off_switch != '~':
            expression = input()
            if expression == '~':
                break

            parser = {self.char1: [total], self.symbol: [], self.char2: []}

            for char in expression:
                if not char.isdigit():
                    parser[self.symbol].append(char)
                    x = expression.split(char)
                    parser[self.char2].append(x[1])
                    break

            off_switch = ''
            total = self.operation_result(parser, parser[self.symbol][0])
            print("--------")
            print(total)

    def operation_result(self, parser, symbol):
        total = 0
        a = int(parser[self.char1][0])
        b = int(parser[self.char2][0])
        op = Operations(a, b)

        if symbol == '+':
            total = op.addition(a, b)
        elif symbol == '-':
            total = op.difference(a, b)
        elif symbol == '*':
            total = op.product(a, b)
        elif symbol == '/':
            total = op.quotient(a, b)

        return total
