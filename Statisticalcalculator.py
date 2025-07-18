import numpy as np

print("welcome to the  statistical calculator program")

def values():
    
    num_List=input("\nplease enter the numbers you want to calculate the statistics for (separated by spaces): ")
    return list(map(float, num_List.split()))


def menu():
    print("\nPlease choose an option:")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Mode")
    print("4. Calculate Standard Deviation")
    print("5. Calculate Variance")
    print("6. Finding the maximum and minimum values.")
    print("7. Exit")


def calculate_mean():
    print("\nCalculating Mean...")
    val=values()
    mean=np.mean(val)
    print(f"The mean is: {mean:.2f}")

def calculate_median():
    print("\nCalculating Median...")
    val=values()
    median=np.median(val)
    print(f"The median is: {median:.2f}")

def calculate_mode():
    print("\nCalculating Mode...")
    arr = values()
    newArr, counts = np.unique(arr, return_counts=True)
    max_count = np.max(counts)
    modes = newArr[counts == max_count]

    if max_count == 1:
        print("No mode found (all values occur only once).")
    elif len(modes) == 1:
        print(f"The mode is: {modes[0]:.2f} (appears {max_count} times)")
    else:
        formatted_modes = ', '.join(f"{m:.2f}" for m in modes)
        print(f"The modes are: {formatted_modes} (each appears {max_count} times)")

def calculate_std_dev():
    print("\nCalculating Standard Deviation...")
    val=values()
    std_dev=np.std(val)
    print(f"The standard deviation is: {std_dev:.2f}")


def calculate_variance():
    print("\nCalculating Variance...")
    val=values()
    variance=np.var(val)
    print(f"The variance is: {variance:.2f}")    

def find_max_min():
    print("\nFinding Maximum and Minimum Values...")
    val=values()
    max_value=np.max(val)
    min_value=np.min(val)
    print(f"The maximum value is: {max_value:.2f}")
    print(f"The minimum value is: {min_value:.2f}")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            calculate_mean()
        elif choice == '2':
            calculate_median()
        elif choice == '3':
            calculate_mode()
        elif choice == '4':
            calculate_std_dev()
        elif choice == '5':
            calculate_variance()
        elif choice == '6':
            find_max_min()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()