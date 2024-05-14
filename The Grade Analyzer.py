#Task 1

list_of_grades = [39, 55, 66, 69, 76, 80, 87, 94, 98]

def average_grade(grade):
    total = sum(grade)
    number = len(grade)
    average = total / number
    return average
print("The average grade is: ", average_grade(list_of_grades))


#Task 2

def highest_and_lowest(grade):
    highest = max(grade)
    lowest = min(grade)
    return highest, lowest

highest_grade, lowest_grade = highest_and_lowest(list_of_grades)
print("The highest grade is: ", highest_grade)
print("The lowest grade is: ", lowest_grade)


#Task 3

def identify_grade(grade):
    if grade >= 88:
        return "A"
    elif grade >= 76:
        return "B"
    elif grade >= 64:
        return "C"
    elif grade >= 52:
        return "D"
    else:
        return "F"
    
letter_grades = [identify_grade(grade) for grade in list_of_grades]
#Prints the letter grades as they correlate with the number grades
print(letter_grades)