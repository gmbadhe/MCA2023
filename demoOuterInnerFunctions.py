def outer():
    message = "Hello"
    
    def inner():
        nonlocal message  # Reference the enclosing variable
        message = "Hello, Python!"  # Modify it
        print("Inside inner:", message)
    
    inner()
    print("Inside outer:", message)

outer()
