
from twilio.rest import Client
account_sid= "AC5186e3d0233838a2236dd8a081a96935"
auth_token= "079a26d27271e7dbd81bc6283e8c1a9c"
client=Client(account_sid,auth_token)
message=client.messages.create(from_='+13082170920',body='hello from twilio',to='+91 8209046716')
print(message.sid)
