import random

while True:

    password_length = 10

    characters = "CLB"
    hdk = '1A2D3E58'
    ldk = '4F5G6H17'
    mdk = '7I8J9K74'
    udk = '0L1M2N8Y5'
    pdk = '3O4P5Q783'
    sdk = '6R7S8T5U0'
    vdk = '9V0W1X0Z1'


    password = "CLB"   

    for index in range(password_length):
        password = password + random.choice(characters + hdk + ldk + mdk + udk + pdk + sdk + vdk)

        print(password)
      