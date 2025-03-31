
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Question 1
print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
question1 = int(input("Enter 1 or 2: "))

if question1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")

# Question 2
print("When I am dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
question2 = int(input("Enter 1-4: "))

if question2 == 1:
    hufflepuff += 2
elif question2 == 2:
    slytherin += 2
elif question2 == 3:
    ravenclaw += 2
elif question2 == 4:
    gryffindor += 2
else:
    print("Wrong input")

# Question 3
print("Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
question3 = int(input("Enter 1-4: "))

if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 == 3:
    ravenclaw += 4
elif question3 == 4:
    gryffindor += 4
else:
    print("Wrong input")

# Final decision
print("Final Scores:")
print("Gryffindor:", gryffindor)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)
print("Slytherin:", slytherin)

max_score = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print("The Sorting Hat has decided...")

if max_score == gryffindor:
    print("Gryffindor!")
elif max_score == ravenclaw:
    print("Ravenclaw!")
elif max_score == hufflepuff:
    print("Hufflepuff!")
else:
    print("Slytherin!")


   



