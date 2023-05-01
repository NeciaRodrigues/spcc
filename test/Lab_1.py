import random

while True:
    choice = int(input('\nEnter your choice : \n1.Create Table\n2.Search Table\n3.Insert a symbol\n4.Remove a symbol\n5.View Table\n6.Exit\n'))
    match choice:
        case 1:
            table = dict()
            symbols = input('\nEnter the statement: ')
            for i in symbols:
                if i not in ['+','-','*','/','=']:
                    typeofChar = 'identifier'
                else:
                    typeofChar = 'operator'
                table[i] = [random.randint(1000, 3000),typeofChar]
        case 2:
            sym = input('\nEnter the symbol to be searched : ')
            if sym in table.keys():
                print(f'Symbol : {sym} Address : {table[sym][0]} Type : {table[sym][1]}')
            else:
                print('Symbol is not present in table')
        case 3:
            sym = input('Enter the symbol to be inserted : ')
            if sym not in table.keys():
                if i not in ['+','-','*','/','=']:
                    typeofChar = 'identifier'
                else:
                    typeofChar = 'operator'
                table[sym] = [random.randint(1000, 3000),typeofChar]
            else :
                print('Symbol already exists')
        case 4:
            sym = input('Enter a symbol to be removed : ')
            if sym in table.keys():
                del table[sym]
            else :
                print('Symbol doesn\'t exist')
        case 5:
            try: 
                if table:
                    for sym in table.keys():
                        print(f'Symbol : {sym} Address : {table[sym][0]} Type : {table[sym][1]}')
            except NameError:
                print('Table is empty')
        case 6:
            break