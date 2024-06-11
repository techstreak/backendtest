from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product
import json


from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Product
from firebase_admin import firestore



from .firestore_api import upload_data_to_firestore



def index(request):
    return render(request, 'index.html')




def get_all_products(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'image_url': product.image_url} for product in products]
    return JsonResponse(data, safe=False)

def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    data = {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'image_url': product.image_url}
    return JsonResponse(data)

'''
def create_product(request):
    if request.method == 'POST':
        try:
            # Extract product data from request
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image_url = request.POST.get('image_url')

            # Log the extracted data
            print("Name:", name)
            print("Description:", description)
            print("Price:", price)
            print("Image URL:", image_url)

            # Create product instance
            new_product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                image_url=image_url
            )

            # Write product data to Firestore database
            success, error = add_product_to_firestore({
                'name': new_product.name,
                'description': new_product.description,
                'price': new_product.price,
                'image_url': new_product.image_url,
                # Add other fields as needed
            })

            if success:
                # Return success response
                return JsonResponse({'message': 'Product created successfully'})
            else:
                # Return error response
                return HttpResponseBadRequest('Error writing to Firestore: {}'.format(error))
        except Exception as e:
            # Log and handle any exceptions
            print('Error creating product:', e)
            return HttpResponseBadRequest('Error creating product: {}'.format(e))

    # Return error response if request method is not POST
    return HttpResponseBadRequest('Invalid request method')
'''


def display_data(request):
    # Retrieve all products from the database
    products = Product.objects.all()

    # Convert product data to list of dictionaries
    data = [{'name': product.name, 'description': product.description, 'price': str(product.price), 'image_url': product.image_url} for product in products]

    # Upload data to Firestore
    success, error = upload_data_to_firestore(data)

    if success:
        return JsonResponse({'message': 'Data uploaded to Firestore successfully'})
    else:
        return HttpResponseBadRequest('Error uploading data to Firestore: {}'.format(error))