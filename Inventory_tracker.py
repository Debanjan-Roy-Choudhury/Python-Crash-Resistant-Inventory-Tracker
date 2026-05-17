print("Crash-Resistant Inventory Tracker".center(40," "))
while True:
    item = input("Enter the Name of the Item (or type 'FINISH' to stop): ")

    if not item:  # Checks if the input is empty
        print("Error: Item name cannot be empty!")
        continue

    if item in ['finish', 'Finish', 'FINISH', 'fINISH']:
        print("Inventory logging complete. Goodbye!")
        break

    print(f"Success: '{item}' has been added to the chart.")
