# Page 1
print("Welcome to page 1!")

# User input
name = input("What is your name? ")

# Process user input
if name:
    message = f"Hello, {name.title()}!"
else:
    message = "Hello, world!"

# Page break
print("\n*** This is a page break. Please turn the page. ***\n")

# Page 2
print("Welcome to page 2!")

# Print the message
print(message)

# Additional message
print("\nThank you for visiting!")
