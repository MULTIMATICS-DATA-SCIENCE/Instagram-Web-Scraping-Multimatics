import instagramy
import re

# Connecting the profile 
session_id = "313961217%3AQ9PNpAQBfnqHO6%3A6"
user = instagramy.InstagramUser("moonyetkecil", sessionid=session_id) 
# printing the basic details like 
# followers, following, bio 
print("Is User is Verified Account?", user.is_verified) 
print("Number of Followers:", user.number_of_followers) 
print("User's Instagram Biography:", user.biography) 
print("Number of Post:",user.number_of_posts)

# return list of dicts
posts = user.posts


print('\n\nLikes', 'Comments') 
for i in range(len(posts)): 
	#likes = posts[post]
	#omments = post["comment"] 
	#print(likes,comments)
	post = str(posts[i])
	find_likes = re.search('likes=(.+?),', post)
	print(find_likes)

post =  instagramy.InstagramPost("BRxTwxeAIGk", sessionid=session_id)

print("Number of likes:", post.number_of_likes)