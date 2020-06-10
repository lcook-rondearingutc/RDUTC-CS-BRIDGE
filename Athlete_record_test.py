# Has a new record been set?

class athlete:
    records = []
    unofficial = []
    def __init__(self, gender, type, record, official):
        self.gender = gender
        self.type = type
        self.record = record
        if official == True:
            athlete.record_list_add(self)
        elif official == False:
            athlete.record_list_add_unofficial(self)

    @classmethod
    def record_list_add(cls, record):
        cls.records.append(record)
    @classmethod
    def record_list_add_unofficial(cls, record):
        cls.unofficial.append(record)
    @classmethod
    def compare(cls):
        message = ""
        records_beat = 0
        for athlete_unofficial in cls.unofficial:
            for record_official in cls.records:
                if athlete_unofficial.gender == record_official.gender or athlete_unofficial.gender == "":
                    if athlete_unofficial.record < record_official.record:
                        records_beat += 1
                        message += f"Athlete in lane {athlete_unofficial.type+1} has beat the {record_official.type} record({record_official.gender}) of {record_official.record}!\n"
        return records_beat, message

    @staticmethod
    def add_records():
        while True:
            gender = input("Athlete gender(m/f): \n>>> ").lower()
            if gender == "m" or gender == "f" or gender == "":
                break
        while True:
            amount = input("How many records would you like to add? (4~8)\n>>> ")
            if amount.isdigit() == True and eval(amount) >= 4 and eval(amount) <= 8:
                amount = int(amount)
                break

        for add_record in range(amount):
            print(f"\nLane {add_record + 1}:")
            while True:
                record_time = input("Enter record time: \n>>> ")
                try:
                    record_time = float(record_time)
                    if record_time > 0:
                        break
                except:
                    pass
            athlete(gender, add_record, record_time, False)

def main():
    athlete("m", "world", 9.58, True)
    athlete("m", "European", 9.86, True)
    athlete("m", "British", 9.87, True)
    athlete("f", "world", 10.49, True)
    athlete("f", "European", 10.73, True)
    athlete("f", "British", 10.99, True)

    athlete.add_records()

    record_amount, record_message = athlete.compare()
    print(f"\nRecords beaten: {record_amount}")
    print(record_message)

if __name__ == "__main__":
    main()
