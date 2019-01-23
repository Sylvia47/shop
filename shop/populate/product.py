from populate import base
from items.models import Category, Product
from unicodedata import category


names = ['喜之坊歐式綿密雪藏蛋糕', 'pan柴奶露麵包海鹽羅宋', '板橋小潘鳳凰酥禮盒']
price = ['50', '50', '50', '50']
categories = ['蛋糕甜點/冰品', '糖果餅乾', '沖泡飲品/飲料']


def populate():
    print('Populating articles and comments ... ', end='')

    for name in names:
        Product = Product()
        Product.name = names
        Product.price = price
        Product.save()
        for Category in categories:
            Product.category = categories
    print('done')


if __name__ == '__main__':
    populate()