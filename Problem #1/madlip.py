def food_input():
    while True:
        user_input = input() 
        tokens = user_input.split()
        
        if tokens[0].lower() == 'quit':
            break
        
        word = tokens[0]
        number = tokens[1]
        
        output = f"Eating {number} {word} a day keeps you happy and healthy."
        print(output)

if __name__ == "__main__":
    food_input()

