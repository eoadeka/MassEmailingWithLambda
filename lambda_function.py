import boto3
import json

print("Loading Function...")

def lambda_handler(event, context):

    ses = boto3.client("ses", region_name="eu-west-2")
    
    sender_email = 'abc@gmail.com'
    recipient_email = 'def@gmail.com'
    
    subject = "Mass emailing with Lambda"
    message = "You are one of the many recipients of this email."
    
    response = ses.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={'Subject': {'Data': subject}, 'Body': {'Text': {'Data': message}}}
    )
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Email sent succesfully!'})
    }
