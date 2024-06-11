# firestore_api.py

from firebase_admin import firestore

def upload_data_to_firestore(products):
    try:
        # Initialize Firestore client
        db = firestore.client()

        # Loop through each product and upload to Firestore
        for product in products:
            doc_ref = db.collection('products').document()
            doc_ref.set(product)
        
        return True, None  # Success
    except Exception as e:
        return False, str(e)  # Error
