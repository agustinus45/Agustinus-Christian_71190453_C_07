from ast import Expression


class PrefixConverter:
    def __init__(self):
        self.stackList = ['+','*','-','/']

    def push(self, e):
        self.stackList.append(e)

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return 'Isi Stack Kosong'

    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return 'Isi Stack Kosong'

    def cekValidExpression(self,expression):
        if expression == self.stackList:
            True
        else:
            return 'Infix yang anda masukkan tidak valid !!'


    def infixToPrefix(self,expression):
        operands = []
		for i in range(len(expression)):
            if (expression[i] == '('):
                self.stackList.append(expression[i])
            elif (expression[i] == ')'):
                while (len(self.stackList)!=0 and self.stackList[-1] != '('):
                    op1 = operands[-1]
                    operands.pop()

                    op2 = operands[-1]
                    operands.pop()

                    op = self.stackList[-1]
                    self.stackList.pop()

                    tmp = op + op2 + op1
                    operands.append(tmp)

                operators.pop()

            elif (not cekValidExpression(expression[i])):
                operands.append(expression[i] + "")

            else:
                while (len(self.stackList)!=0 ):
                    op1 = operands[-1]
                    operands.pop()

                    op2 = operands[-1]
                    operands.pop()

                    op = self.stackList[-1]
                    operators.pop()

                    tmp = op + op2 + op1
                    operands.append(tmp)
                self.stackList.append(expression[i])
		
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix('1+2+3*4/2-1'))
    print(expresi1.infixToPrefix('A * (B + C) / D'))
    print(expresi1.infixToPrefix(''))
    print(expresi1.infixToPrefix())
    print(expresi1.infixToPrefix())

    