
class Mon():
    def __init__(self, start):
        self.month = start
        self.months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']

    def get_next_month(self):
        if self.month == 12:
            self.month = 1
            return self.month
        self.month = self.month + 1
        return self.month

