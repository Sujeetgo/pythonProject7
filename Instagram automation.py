from instabot import Bot
bot = Bot()
user_1 = input(" enter your username: ")
pass_1 = input(" enter your password: ")

user = bot.login(username= user_1, password=pass_1)

user_2 = input(" Enter the username you want to follow:   ")

#bot.follow(user_2)
photo_1 = input(" Enter the path of the photo you want to upload: ")  # ##path should br in forward slace and end with name of photo .py

#bot.upload_photo(photo_1, caption=" My new Post")

unfollow_2 = input(" Enter user to unfollow:  ")

#bot.unfollow(unfollow_2)

msg= input("enter you message to send : ")

msg_to_send = input(" enter username to whom you want to send message: ")   ### username should be comma seprated
 # bot.send_messages(msg, msg_to_send)

# followers = bot.get_user_followers(user_1)
# for follower in followers:
#     print(bot.get_user_followers(follower))


following= bot.get_user_following(user_1)
for Following in following:
    print(bot.get_user_info(Following))

    











