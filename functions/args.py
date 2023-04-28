def my_country(country="Rwanda"):
    print(f"Hello from{country}")

def greet(*name):
    for name in name:
        print(f"hello{name}")

def sum(*number):
    answer = 0
    for num in number:
     answer+= num
    
    return answer


def product(*value):
    answer = 1
    for number in value:
        answer*=number
    return answer

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

        # A function named concatenate_args that takes any number of string arguments in 
# positional arguments format and concatenates them into a single string
def concatenate_args(*args):
    return "".join(args)
result = concatenate_args()
print(result) 

# A function named concatenate_kwargs that takes any number of string arguments in 
# keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kids):
    return "".join(kids.values())
Output = concatenate_kwargs()
print(Output) 
