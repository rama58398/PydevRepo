# def make_shirt(size , message="I love python"):
#     """Display the size and message of the shirts that to be printed """
#     if size.lower().strip()=='l':
#         msg="The planet earth"
#         make_shirt('l',msg)
#         print(f"The message of the shirt {msg}")
#         break
#     else:
#         print(f"The size of the shirt is {size.title().strip()} ")
#
# make_shirt('M',message="I love python")
# make_shirt('s')
# make_shirt(size="l",message="Occupy Mars")

# def city_country(city,country):
#     details= {'City': city, 'Country': country}
#     return details
# country_details=city_country("columbus","usa")
# print(country_details)

# def make_album(artist, album,No_of_songs=None):
#     song_name={'Artist':artist,'Album':album,'Number of Songs':No_of_songs}
#     return song_name
# print(make_album('rehman','boys',2))
# print(make_album('keer','rrr'))
# print(make_album('kate','roar'))


# def greet_users(names):
#     for name in names:
#         print("hello ",name)
#
# users=['x','y','z']
# greet_users(users)

#
# def un_printed_list(un_printed):
#     while un_printed:
#         current_print=un_printed.pop()
#         print("current_print",current_print)
#         completed_printing.append(current_print)
#
# def completed_print(completed_printing):
#     for current in completed_printing:
#         print("completed_printing",current)
# un_printed=['starbucks','super cuts','north star']
# completed_printing=[]
#
# un_printed_list(un_printed[:])
# completed_print(completed_printing)
# print(un_printed)

# def send_messages(message_send,sent_messages):
#     while message_send:
#         curr_messages=message_send.pop()
#         print("curr_messages",curr_messages)
#         sent_messages.append(curr_messages)
#
# def show_messages(sent_messages):
#     for message in sent_messages:
#         print('show_messages',message)
#
# message_send=['hi','how are you ','come over ']
# sent_messages=[]
# send_messages(message_send[:],sent_messages)
# show_messages(sent_messages)


# def person_want_sandwich(*items):
#     print("the summary of items in sanwich ordered ",items)
#
# person_want_sandwich('veg','non-veg')
# person_want_sandwich('veg','meat','egg')
#
# person_want_sandwich('veg','meat','egg','chicken','turkey')

# def build_profile(firstname,lastname,**userinfo):
#     userinfo['first']=firstname
#     userinfo['last']=lastname
#     return userinfo
# user_profile=build_profile('al','val',loc= 'in',id=10)
#
# print(user_profile)

