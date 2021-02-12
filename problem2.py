grades = float(input("what grades did you receve last year: "))
wages = float(input("what wages did you earn last year: "))
 
if grades >= 80 and wages >= 500:
    print("You get to go to Europe.")
elif grades >= 80:
    print("You get to go to California.")
else:
    print("You must stay home ")
