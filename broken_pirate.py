greeting = input("Hello, possible pirate! What's the password? ")  # Fixed unclosed string

if greeting in ["Arrr!"]:  # Fixed list syntax
    print("Go away, pirate.")
else:  # Replaced the broken 'elif' with 'else'
    print("Greetings, hater of pirates!")
