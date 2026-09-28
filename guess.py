import random
secret= random.randint(1,100)
while True:

    g = int(input("try to guess the number :- "))
    if g > secret:
        print("bro come little down")
    elif g< secret:
        print("bro come little up ")
    else:
        print("bro u actually made it !!!! well done now do some study \n why are u wasting time 🥲")
        break 
      