class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, amount):
        self.bill_amount = amount

    def calculate_bill(self):
        return self.bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        total = super().calculate_bill()
        return total - (total * .20)


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        total = super().calculate_bill()
        return total - (total * .15)


regular_patient = Patient("Jean Maxine Delos Santos", 15000)
senior_patient = SeniorPatient("Ezavella D. Guillermo", 15000)
philhealth_patient = PhilHealthPatient("Rachel Bocalan", 15000)

print("Hospital Billing System")
print("-------------------------")
print("Patient Name:", regular_patient.get_name())
print(f"Bill Amount: {regular_patient.get_bill_amount():,.2f}")
print(f"Calculated Bill: {regular_patient.calculate_bill():,.2f}")

print(f"\nSenior Patient:")
print("Patient Name:", senior_patient.get_name())
print(f"Bill Amount: {senior_patient.get_bill_amount():,.2f}")
print(f"Calculated Bill: {senior_patient.calculate_bill():,.2f}")

print(f"\nPhilHealth Patient:")
print("Patient Name:", philhealth_patient.get_name())
print(f"Bill Amount: {philhealth_patient.get_bill_amount():,.2f}")
print(f"Calculated Bill: {philhealth_patient.calculate_bill():,.2f}")
