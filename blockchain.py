blockchain = [1]


def add_value(num):
    blockchain.append([blockchain[-1], num])
    print(blockchain)


# add_value(10)
# add_value(20)
# add_value(30)
# add_value(40)
# add_value(50)


def addNum(num1, num2):
    return num1 + num2


print(addNum(3, 5))
