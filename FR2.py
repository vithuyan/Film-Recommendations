documentaries = "Icarus"
drama = "Room"
comedy = "TAG"
dramedy = "Juno"

print ("Rate the following from 1 to 5.")
print ("How would you rate documentaries?")
documentary_rating = input()
print ("How would you rate dramas?")
drama_rating = input()
print ("How would you rate comedy?")
comedy_rating = input()


if int(documentary_rating) >= 4:
    print ("Watch Icarus.")

if int(documentary_rating) <= 3  and int(comedy_rating) >= 4 and int(drama_rating) >= 4:
    print ("Watch Juno.")

if int(drama_rating) >= 4:
    print ("Watch Room.")

if int(comedy_rating) >= 4:
    print ("Watch TAG.")

if int(drama_rating) <= 3 and int(comedy_rating) <= 3 and int(documentary_rating) <= 3:
    print ("Read Harry Potter")
