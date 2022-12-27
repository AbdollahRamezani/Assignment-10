class Date:
   #properties 
    def __init__(self, day, month, year, hour, minute, seconds):
        self.minute = minute
        self.seconds = seconds
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
       
        self.check_valid_inputs()
   #methods     
    def convert_to_miladi_date(self, date):
        ...
    def check_valid_inputs():
        ...
    
    def convert_to_shamsi_date(self, date):
        ...
    
    def convert_to_ghamari_date(self, date):
        ...