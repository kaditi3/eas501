# Define molecular weights
MW_sucrose = 342.30  # g/mol
MW_glucose = 180.18  # g/mol
MW_ethanol = 46.08   # g/mol
MW_CO2 = 44.01       # g/mol
MW_CH4 = 16.04       # g/mol

# Percentage of sucrose in molasses by weight
sucrose_content = 0.50  # 50%


def calculate_molasses_required_for_methane():
    """Calculate amount of molasses required for a specific amount of methane."""
    try:
        # Get input
        desired_methane_kg = float(input("Enter the desired amount of methane in kilograms: "))
        
        # Calculations
        desired_methane_g = desired_methane_kg * 1000
        moles_CH4_required = desired_methane_g / MW_CH4
        moles_ethanol_required = (2 / 3) * moles_CH4_required
        moles_glucose_required = moles_ethanol_required / 2
        moles_sucrose_required = moles_glucose_required / 2
        mass_sucrose_required = moles_sucrose_required * MW_sucrose
        mass_molasses_required = mass_sucrose_required / sucrose_content
        mass_molasses_required_tonnes = mass_molasses_required / 1000000
        
        # Output
        print(f"Total molasses required: {mass_molasses_required_tonnes:.3f} metric tonnes")
    except ValueError:
        print("Please enter a valid number.")


def calculate_CO2_and_CH4_from_molasses():
    """Calculate the amount of CO2 and CH4 produced from a given amount of molasses."""
    try:
        # Get input
        molasses_mass_tonnes = float(input("Enter the amount of molasses in metric tonnes: "))
        molasses_mass_g = molasses_mass_tonnes * 1000000
        
        # Calculations
        sucrose_mass = molasses_mass_g * sucrose_content
        moles_sucrose = sucrose_mass / MW_sucrose
        moles_glucose = 2 * moles_sucrose
        moles_ethanol = 2 * moles_glucose
        moles_CH4 = 1.5 * moles_ethanol
        moles_CO2_from_glucose = 2 * moles_glucose
        moles_CO2_from_ethanol = 0.5 * moles_ethanol
        total_moles_CO2 = moles_CO2_from_glucose + moles_CO2_from_ethanol
        total_mass_CO2_kg = (total_moles_CO2 * MW_CO2) / 1000
        total_mass_CH4_kg = (moles_CH4 * MW_CH4) / 1000
        
        # Output
        print(f"CO2 produced: {total_mass_CO2_kg:.3f} kilograms")
        print(f"CH4 produced: {total_mass_CH4_kg:.3f} kilograms")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main function to run the program."""
    print("Choose an option:")
    print("1. Calculate molasses required for a specific amount of methane")
    print("2. Calculate CO2 and CH4 produced from molasses")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        calculate_molasses_required_for_methane()
    elif choice == "2":
        calculate_CO2_and_CH4_from_molasses()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
    
