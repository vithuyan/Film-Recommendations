documentaries = "Icarus"
drama = "Room"
comedy = "TAG"
dramedy = "Juno"

print (" Do you enjoy documentaries, dramas or comedy?")
user_name = input()
if user_name == "documentaries":
  print("You should watch {}.".format(documentaries))

if user_name == "drama":
  print("You should watch {}.".format(drama))

if user_name == "comedy":
  print("You should watch {}.".format(comedy))

if user_name == "dramedy":
  print("You should watch {}.".format(dramedy))

else:
  print("read Harry Potter" )
