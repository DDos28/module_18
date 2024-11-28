from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    shop_items = {
        'items': [
            {'name': 'Игра A', 'price': '10$', 'button_text': 'Купить'},
            {'name': 'Игра B', 'price': '15$', 'button_text': 'Купить'},
            {'name': 'Игра C', 'price': '20$', 'button_text': 'Купить'},
        ]
    }
    return render(request, 'third_task/shop.html', context=shop_items)

def cart(request):
    cart_items = [
        {'name': 'Игра A', 'price': 10, 'quantity': 1},
        {'name': 'Игра B', 'price': 15, 'quantity': 2},
    ]
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'third_task/cart.html', context=context)