# Exception Handling
# Write a program that asks for two numbers and divides them

# if   =  try
# elif =  except with erroe type
# else =  except
try:    # we always enter the try block, there is no condition
   x = int(input("what is the first number?\n>"))
   y = int(input("what is the second number?\n>"))
   print(x / y)
   
except ZeroDivisionError:
   print("cannot divide by zero, try again")
   divide_two_numbers()

except ValueError:
   print:("please enter a valid numerical symbol try again.")
         divide_two_number()
   
except: # If anything in the try block cause an error
   # the try block stops immediately and the exept is ran instead
   # the rest of the block never finishes running, its skipped
   # if the try block executes without an error, the except is skipped
   # the only way to get into the except is to "throw" an error
   print("Invalid input, try again.")
   divide_two_numbers()   # Tell the function to run again

   divide_two_numbers()
