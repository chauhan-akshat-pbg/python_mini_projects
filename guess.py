import random


play ="yes"
while play== "yes":
            secret= random.randint(1,100)
            attempt=0
            while True:

                try:
                    g = int(input("try to guess the number :- "))
                except ValueError:
                    print("bro type an actual number")
                    continue
                
                if g > secret:
                    print("bro come little down")
                elif g< secret:
                    print("bro come little up ")
                else:
                    print("bro u actually made it !!!! well done now do some study \n why are u wasting time 🥲")
                    break 
                attempt +=1
            print("bro you took ",attempt," attempts seriously")
            play=input("Do u want to play again (yes/no): ")