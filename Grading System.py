# Range of marks defined as a list
marks_range=[0,20,40,60,80,100,120] 

# Initializing count variables
progress_count=0
trailer_count=0
exclude_count=0
retriever_count=0

# Creating lists for store user inputs
inputs = []
all_inputs=[]

# Define a function to validate the credit inputs
def validation(credit):
        try:
                credit=int(credit)
                if credit not in marks_range:
                        print("Out of range")
                        return False
                else:
                        return credit
        except ValueError:
                print("Integer required")
                return False

# Define a function for students to input theire credits and get the progression outcome
def student():

        # Declaring global variables that use across different functions to track counts and progression details
        global progress_count, trailer_count, exclude_count, retriever_count, pass_credits, defer_credits, fail_credits, progression
        
        # Getting pass credits and validate
        while True:
                pass_credits=(input("\nPlease Enter your credit at pass :"))
                pass_credits=validation(pass_credits)
                if pass_credits is False:
                    continue
                else:
                    break

        # Getting defer credits and validate
        while True:
                defer_credits=(input("Please Enter your credit at defer :"))
                defer_credits=validation(defer_credits)
                if defer_credits is False:
                    continue
                else:
                    break

        # Getting fail credits and validate
        while True:
                fail_credits=(input("Please Enter your credit at fail :"))
                fail_credits=validation(fail_credits)
                if fail_credits is False:
                    continue
                else:
                    break

        # Check if the total credits are correct
        total = pass_credits + defer_credits + fail_credits
        if total != 120:
                print("Total incorrect")
                student()
                  
        # Determine the progression outcome according to the credits and updating counting variables
        elif pass_credits == 120:
                print("\nProgress")
                progress_count += 1
                progression = "Progress"
                
        elif pass_credits == 100 and (defer_credits == 20 or fail_credits == 20):
                print("\nProgress(module trailer)")
                trailer_count += 1
                progression = "Progress(module trailer)"
                
        elif fail_credits >= 80:
                print("\nExclude")
                exclude_count += 1
                progression = "Exclude"
                
        else:
                print("\nModule Retriever")
                retriever_count += 1
                progression = "Module Retriever"