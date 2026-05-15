import json
import requests

def handle_webhook(payload):
    data = json.loads(payload)
    name = data['name']
    email = data['email']
    message = data['message']
    
    response = requests.post('https://api.example.com/leads', {
        'name': name,
        'email': email,
        'message': message
    })
    
    if response == 200:
        print("Lead saved successfully")
        return True
    else:
        print("Failed to save lead")
        return False

def classify_enquiry(text):
    keywords = ['order', 'complaint', 'refund', 'shipping', 'delivery']
    for word in keywords:
        if word in text:
            return word
    return 'general'

def send_confirmation(email, booking_ref):
    msg = "Dear customer, your booking " + booking_ref + " is confirmed."
    requests.post('https://api.example.com/email', {
        'to': email,
        'body': msg
    })
