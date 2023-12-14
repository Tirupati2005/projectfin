from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from .models import Product, Order
import io
import base64

def visual_representation(request):

    products = Product.objects.all()
    order_count = []

    for product in products:
        orders = Order.objects.filter(product=product)
        order_count.append({'Product': product.name, 'OrderCount': orders.count()})

    df = pd.DataFrame(order_count)

    plt.figure(figsize=(10, 6))
    plt.bar(df['Product'], df['OrderCount'], color='skyblue')
    plt.xlabel('Product')
    plt.ylabel('Number of Orders')
    plt.title('Product Popularity based on Orders')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')
    image = f"data:image/png;base64,{graphic}"

    return render(request, 'store/product_popularity.html', {'image': image})

