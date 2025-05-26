# Input handling .v0.01
# Set your default values in class init block
# If error: return default_value of a specific type

# EXAMPLE:
# - set your age

# error = CheckValue()
# age = error.get_int()

# if input isn't int return default value (1)
# else return user value


class CheckValue:
# setting default values
    def __init__(self):
#default INT
        self.d_i = 1
#default STR
        self.d_s = '[Empty_string]'
#default BOOL
        self.d_b = True

# INT---
    def get_int(self):
        try:
            value = int(input())
            return value
        except:
            return self.d_i    # returning default value

# STR---   
    def get_str(self):
        value = input()
        if value == "" or value is None:
            return self.d_s
        try:
            str(value)
            return value
        except:
            return self.d_s    # returning default value
            
# BOOL---            
    def get_bool(self):
        value = input()
        if value == 1 or value == 0 or value == '1' or value == '0':
            if value == '0': 
                value = False
            return bool(value)
        
        return self.d_b    # returning default value
        
    
    
# Unit tests:

#    SETTINGS 
error = CheckValue()      # object init
number = None             # argument returns 1
string = ''               # argument returns '[Empty_string]'
logical_value = 's'       # argument returns True (default bool)
#---

print(error.get_int())
print(error.get_str())
print(error.get_bool())