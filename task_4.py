class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


# Пример использования:

employee1 = EmployeeSalary.get_hours("Алексей", None, 2, "alex@example.com")
print(employee1.hours)  # 40
print(employee1.email)  # alex@example.com
print(employee1.salary())  # 16000

employee2 = EmployeeSalary.get_email("Ирина", 35, 1, None)
print(employee2.email)  # Ирина@email.com
print(employee2.salary())  # 14000

EmployeeSalary.set_hourly_payment(500)
print(employee1.salary())  # 40 * 500 = 20000
print(employee2.salary())  # 35 * 500 = 17500
