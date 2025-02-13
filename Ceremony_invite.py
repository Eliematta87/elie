fname = input("Enter your first name: ") # global

# build in methods & functions - print, len, type...

def this_is_my_function(fname): # local
    # block of function code
    #print(f"Hello {fname}")
    return f"\nhello {fname}"
#this_is_my_function(fname)
new_var = this_is_my_function(fname)
print(new_var)


def my_function(fname):
    print(fname + "ceremony.")

#my_function("elie")
#my_function("michael")
#my_function("mila")
my_function("you are invited to our marriage ")


names = ["elie", "daniel"]

def my_function(couple):  # new_name = ["elie", "zakaa"] = placeholder (argument)
             # ["elie", "zakaa"] = parameter
             #     0  ,   1
    #groom = new_name[0]
    #bride = new_name[1]
    groom = couple[0]
    bride = couple[1]
    #print(f"{groom} and {bride} are getting married tonight")
    return f"{groom} and {bride} are getting married tonight. \n{groom} is the groom and {bride} is the bride.\n thank you for coming to our wedding."
    #return f"{groom} and {bride} are getting married tonight"

#x = my_function(["elie", "zakaa"])
x = my_function(names)  # ["elie", "zakaa"]

print(x)
