is_magician = False
is_expert = True 

#check if magician and expert: "you are a master magician"

if is_expert and is_magician: 
  print("you are a master magician")

#check if magician but not expert: "at least you are getting there"
  
elif is_magician and not is_expert:
  print("at least you're getting there")
  
#if you're not a magician: "You need magic powers"

elif not is_magician: 
  print("You need magic powers")

#my answers
# if is_magician and is_expert:  
#  print("you are a master magician")
# elif is_expert:
#   print("at least you are getting there")
# else: 
#   print("You need magic powers")