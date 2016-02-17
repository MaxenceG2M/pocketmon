from pocket import Pocket

request_token = Pocket.get_request_token("44479-ea92cc886eed9b46660b84a4")
print(request_token)

# URL to redirect user to, to authorize your app
auth_url = Pocket.get_auth_url(request_token)
print(auth_url)

user_credentials = Pocket.get_credentials("44479-ea92cc886eed9b46660b84a4", request_token)
print(user_credentials)

access_token = user_credentials['access_token']
print(access_token)
