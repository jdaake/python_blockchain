blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(trans_amount, last_transaction=[1]):
    blockchain.append([last_transaction, trans_amount])


def get_transaction_value():
    """Gets the user input for the transaction amount. """
    return float(input('Enter the transaction amount: '))

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_element():
    for block in blockchain:
        print('Outputting Block')
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Print blockchain')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_element()
    
print('done')


