def calculate_pi(iterations):
    pi = 0
    for i in range(iterations + 1): 
        pi += (-1)**i / (2*i + 1)  
    return round(4 * pi, 2)  

def main():
    print("Welcome! Calculate an approximate value of Pi.")
    try:
        user_input = input("Enter iterations (0 or more) or 'quit' to exit: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            return
        iterations = int(user_input)
        if iterations < 0:
            print("Error: Iterations must be 0 or more.")
        else:
            print(f"Approximation of Pi after {iterations} iterations: {calculate_pi(iterations)}")
    except ValueError:
        print("Error: Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
