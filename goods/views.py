from django.shortcuts import render

def catalog(request):
    context = {
        "title": "Home - Catalog",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Tea Table and Three Chairs",
                "description": "A set of three chairs and a designer table for the living room.",
                "price": 150.00
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Tea Table and Two Chairs",
                "description": "A minimalist-style set of a table and two chairs.",
                "price": 93.00
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Double Bed",
                "description": "A double bed with a headboard and excellent orthopedic design.",
                "price": 670.00
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Kitchen Table with Sink",
                "description": "A dining table with a built-in sink and chairs.",
                "price": 365.00
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Kitchen Table with Built-In Appliances",
                "description": "A kitchen table with a built-in stove and sink. Many shelves and a beautiful design.",
                "price": 430.00
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Corner Sofa for Living Room",
                "description": "A corner sofa that converts into a double bed, perfect for the living room and hosting guests!",
                "price": 610.00
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Bedside Table",
                "description": "A bedside table with two drawers (flower not included).",
                "price": 55.00
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Ordinary Sofa",
                "description": "A sofa, also known as a standard couch, with nothing remarkable to describe.",
                "price": 190.00
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Office Chair",
                "description": "A description of how great it is, but it's just a chair, so not much to say...",
                "price": 30.00
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Plant",
                "description": "A plant to decorate your interior, bringing freshness and tranquility to the atmosphere.",
                "price": 10.00
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Stylized Flower",
                "description": "A designer flower (possibly artificial) for interior decoration.",
                "price": 15.00
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Night Table",
                "description": "A table with a rather strange appearance, but suitable for placing beside a bed.",
                "price": 25.00
            }
        ]
    }

    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')
