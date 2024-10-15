def free_shipping(age, consent, member):
    if age >= 18 and consent == True and member == True:
        print("BET you can have free shipping")

    else:
        print("yeah man you AINT getting free shipping")

free_shipping(18, True, True)
