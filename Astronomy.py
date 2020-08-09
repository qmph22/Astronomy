def Find_Theta_Arcseconds(actual_size_lyr, distance_lyr):
    return 206265 * (float(actual_size_lyr)/float(distance_lyr))
def Find_Distance_Light_Years(angular_size_theta, actual_size_lyr):
    return 206265 * float(actual_size_lyr)/float(angular_size_theta)
def Find_Actual_Size_Light_Years(angular_size_theta, distance_lyr):
    return (float(angular_size_theta) * float(distance_lyr))/206265
def Convert_Parsec_to_Light_year(parsec):
    return float(parsec) / 3.26
def Convert_Light_Year_to_Parsec(light_year):
    return float(light_year) * 3.26
def Find_Parsec(arcsec):
    return float(1/arcsec)
def Find_Parsec(arcminute):
    return float(1/(arcminute*60))

def Small_Angle_Approximation_Calculation_Prompt():
    while True:
        try:
            option = int(input("""Please select an option:
1. Find the angular size in arcseconds using the actual size and distance in light years.
2. Find the actual size in light years using the angular size in arcseconds and distance and light years.
3. Find the distance in light years using the angular size in arcseconds and distance in light years.
4. Exit.
> """))
            if option > 0 and option <= 4:
                break
            else:
                print("Incorrect input. Try again.")
        except:
            print("Incorrect input. Try again.")
    was_lyr = False
    if option == 1:
        actual_size_lyr = float(input("What is the actual size of this object in light years? "))
        distance_lyr = float(input("What is the distance of this object in light years? "))
        answer_arcseconds = Find_Theta_Arcseconds(actual_size_lyr, distance_lyr)
        print(f"The answer is {answer_arcseconds.__str__()} arcseconds.")
    elif option == 2:
        distance_lyr = float(input("What is the distance of this object in light years? "))
        angular_size_theta = float(input("What is the angular size of this object in arcseconds? "))
        answer_lyr = Find_Actual_Size_Light_Years(angular_size_theta, distance_lyr)
        was_lyr = True
        print(f"The answer is {answer_lyr.__str__()} light years.")
    elif option == 3:
        actual_size_lyr = float(input("What is the actual size of this object in light years? "))
        angular_size_theta = float(input("What is the angular size of this object in arcseconds? "))
        answer_lyr = Find_Distance_Light_Years(angular_size_theta, actual_size_lyr)
        was_lyr = True
        print(f"The answer is {answer_lyr.__str__()} light years.")
    elif option == 4:
        print("Exiting.")
    if was_lyr:
        parsec_prompt_result = False
        while parsec_prompt_result != True:
            parsec_prompt = input("Would you like this answer in Parsecs? Y/N ").__str__().capitalize()
            if parsec_prompt == "Y":
                print(f"The answer is {(answer_lyr * 3.26).__str__()} parsecs.")
                parsec_prompt_result = True
                break
            elif parsec_prompt == "N":
                parsec_prompt_result = True
                break
            else:
                print("Invalid input. Please try again.")