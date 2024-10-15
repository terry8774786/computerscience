# if statements evaluate baoolean expressins !
# they make decisions about which code to run next

# Take a temperature
# print "<Temperature> is hot" if its >=80
# Otherwise, print "<temperature is not hot"
temp = input("what the temperature in F?\n>")
temp = int(temp)

#If <boolean expression>:
# This should remind of writting aq fuction
#def <name>():
if temp >= 80:
   print(str(temp) + "0 is hot !")

   if temp < 80:
      print(str(temp) + "0 is not hot...")
   
   else:    # Otherwise....
      print(str(temp) + "0 is not hot...")

# Not all if statements need an else, in fact NONE of them NEED and else
# Else statement are an option, they are optional
# All else statements must have a corresponding if statement 
# Elseif statements cannot exist alone
# An if statement can only have one  ELSE

# Create a program that asks for a password
# If the password if correct. print ACCESS GRANTED
# Otherwise, print ACCESS DENIED
# The password is skibidi68

real_pass = "skibidi68"
input_pass = input("whats the password?\n>")

if input_pass == real_pass:
     print("ACCESS GRANTED")
else:
    print("dontmoveoryougetsnapfromamileaway")


# Activity 2, electric boogaloo
# Create a five question quiz that prints your score at the end 
# choose any five questions


print("math Test\n")

score = 0

anser_one = input("what is 2 + 2\n>")
answer_one = int(answer_one)
if answer_one == 4:
    score
