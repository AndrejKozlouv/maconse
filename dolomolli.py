try:
    # code that may raise an exception
except (ValueError, IndexError) as e:
    # code to handle both ValueError and IndexError exceptions
    print(f"An error occurred: {e}")
finally:
    # code that will always be executed
