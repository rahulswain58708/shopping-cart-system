#shopping cart system.
'''features:
1.add product.
2.buy product.
3.view product.
4.Exit
'''
products = []
while True:
    print('-----Amazon shoping cart------')
    print('Options:add/buy/view/exit')
    option = input('Choose one option:')
    if option == 'add':
        product = input('Enter Product to add:')
        products.append(product)
        print(f'product {product} added succesfull.')
    elif option == 'buy':
        product = input('Enter product to buy:')
        if product not in products:
            print('Product not available')
        else:
            products.remove(product)
        print(f'product {product} buy sucessfull🎉.')
    elif option == 'view':
        print(f'products:\n{products}')
    elif option == 'exit':
        print('Exit shoping cart✅.')
        break
    else:
        print('Invalid option')
    
