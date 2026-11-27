class Expense:
    def __init__(self, title, amount, category, date, payment_method):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.payment_method = payment_method

    def __str__(self):
        return f"{self.title} - PHP {self.amount:.2f} ({self.category})"
