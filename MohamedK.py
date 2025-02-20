
import os    
    # Get the current working directory 
    
current_directory = os.getcwd()
    
print("Current working directory:", current_directory)
    
    # List all files in the current directory
    
print("\nFiles in the current directory:")

    
for file in os.listdir():
        
    print(file)
    