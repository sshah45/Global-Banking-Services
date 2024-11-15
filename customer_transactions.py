import csv
from datetime import date, datetime
from fpdf import FPDF
from typing import List, Tuple, Dict


class Customer:  # Data-Oriented Class.
    def __init__(
        self,
        name: str,
        contact: str,
        acc_num: str,
        password: str,
        pin: str,
        balance: int = 1000,
        record: int = 0,
        date=None,
        time=None,
    ):
        self.name = name
        self.contact = contact
        self.acc_num = acc_num
        self.password = password
        self.pin = pin
        self.balance = balance
        self.record = record
        self.date = date
        self.time = time

    def store_data(self, filename: str, fieldnames: List[str], data: Dict[str, str]):
        # Helper method to store data into CSV.
        try:
            with open(filename, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(data)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

    def store_data1(self):
        # Stores basic customer info in 'input_data1.csv.
        data = {
            "name": self.name,
            "contact": self.contact,
            "acc_num": self.acc_num,
            "password": self.password,
            "pin": self.pin,
        }
        self.store_data(
            "input_data1.csv", ["name", "contact", "acc_num", "password", "pin"], data
        )
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        print(f"\nAccount Created Successfully! On {self.date} at {self.time}")

    def store_data2(self):
        # Stores customer transaction record in 'input_data2.csv'.
        data = {
            "date": self.date,
            "time": self.time,
            "record": self.record,
            "acc_num": self.acc_num,
            "balance": self.balance,
        }
        self.store_data(
            "input_data2.csv", ["date", "time", "record", "acc_num", "balance"], data
        )


class Transactions:  # Method-Oriented Class.
    def __init__(self, name: str, acc_num: str, pin: str, date=None, time=None):
        self.name = name
        self.acc_num = acc_num
        self.pin = pin
        self.date = date
        self.time = time
        self.record, self.balance, self.transactions = self.find_acc()

        self.closing_balances: List[
            int
        ] = []  # Will be the list of a 'Closing Balance' after each transactions.
        self.date_time: List[
            Dict[str, str]
        ] = (
            []
        )  # Will be the list of a dictionaries having keys ('date' and 'time') of a transactions.
        self.statement_related: List[
            Dict[str, str]
        ] = (
            []
        )  # Will be the list of a dictionaries having keys ('credit_or_debit', 'closing', 'date' and 'time')

    def __str__(self) -> int:
        return self.balance

    def find_acc(
        self,
    ) -> tuple[
        int, int, list[Dict[str, str]]
    ]:  
        row = 0  # To know at which row (of the csv) the acc_num matches.
        all_transactions = []
        try:
            with open("input_data2.csv") as f1:
                reader = csv.DictReader(f1)
                data = list(reader)

                for dictionary in data:
                    row += 1
                    if self.acc_num == dictionary["acc_num"]:
                        all_transactions.append(data[row - 1])
                        continue

                    else:
                        continue

                all_transactions = sorted(
                    all_transactions,
                    key=lambda all_transactions: int(all_transactions["record"]),
                    reverse=True,
                )
                mostrecent_transaction = all_transactions[0]

                return (
                    int(mostrecent_transaction["record"]),
                    int(mostrecent_transaction["balance"]),
                    all_transactions,
                )
        except FileNotFoundError:
            print("Error: File not found.")

    def write_record(self):
        # Writes transaction details to 'input_data2.csv'.
        data = {
            "date": self.date,
            "time": self.time,
            "record": self.record,
            "acc_num": self.acc_num,
            "balance": self.balance,
        }

        try:
            with open("input_data2.csv", "a") as f2:
                writer = csv.DictWriter(
                    f2, fieldnames=["date", "time", "record", "acc_num", "balance"]
                )
                writer.writerow(data)
        except FileNotFoundError:
            print("Error: File not found.")

    def deposit(self, amount: int, pin: str):  # Deposits money into the account.
        if pin == self.pin:
            self.record += 1
            self.balance += amount
            self.date = date.today()
            self.time = datetime.now().strftime("%H:%M:%S")
            return self.balance

        else:
            print("\nIncorrect Pin❗")
            return False

    def withdraw(self, amount: int, pin: str):  # Withdraws money from the account.
        if pin == self.pin:
            if amount <= self.balance:
                self.record += 1
                self.balance -= amount
                self.date = date.today()
                self.time = datetime.now().strftime("%H:%M:%S")
                return self.balance

            else:
                print("\nInsufficient Balance In Your Account❗")
                return "Insufficient!"
        else:
            print("\nIncorrect Pin❗")
            return "Incorrect Pin!"

    def append_transactions(
        self,
    ):  # Appends previous transactions to internal lists in 'init'.
        for transaction in self.transactions:
            self.closing_balances.append(transaction["balance"])
            self.date_time.append(
                {"date": transaction["date"], "time": transaction["time"]}
            )

    def generate_statement(
        self,
    ):  # This method is resposible for creating all the necessary information regarding the statement.
        for i in range(len(self.closing_balances) - 1):
            change = int(self.closing_balances[i]) - int(self.closing_balances[i + 1])

            self.statement_related.append(
                {
                    "credit_or_debit": change,
                    "closing": int(self.closing_balances[i]),
                    "date": self.date_time[i]["date"],
                    "time": self.date_time[i]["time"],
                }
            )

        self.create_pdf()

    def create_pdf(self):  # Generates a PDF statement.
        customer_name = self.name
        customer_accnum = self.acc_num
        transaction_date = date.today()
        records = self.statement_related[:20]

        class PDF(FPDF):  # Sub-class of FPDF.
            def header(self):
                self.set_font("Times", "", 12)
                self.set_y(10)
                self.cell(48)
                self.cell(None, None, "GLOBAL BANK ACCOUNT STATEMENT", align="C")
                self.ln(15)
                self.set_font("Times", "", 10)
                self.cell(5)
                self.cell(None, None, f"Account Name :  {customer_name}", align="L")
                self.ln(5)
                self.cell(5)
                self.cell(None, None, f"Account Number :  {customer_accnum}", align="L")
                self.ln(5)
                self.cell(5)
                self.cell(None, None, f"Date :  {transaction_date}", align="L")
                self.ln(10)
                self.cell(5)
                self.cell(None, None, f"Account Summary", align="L")
                self.ln(5)
                self.cell(5)
                self.cell(None, None, f"Past Transactions(Max 20)")
                self.ln(10)

                self.form_table()

            def form_table(self):
                with self.table() as table:
                    row = table.row()
                    row.cell("Transaction(Date&Time)")
                    row.cell("Debit (in ruppes)")
                    row.cell("Credit (in ruppes)")
                    row.cell("Closing Balance (in ruppes)")

                    for rec in records:
                        if rec["credit_or_debit"] > 0:
                            row = table.row()
                            row.cell(f"On {rec['date']} At {rec['time']}")
                            row.cell("")
                            row.cell(f"{rec['credit_or_debit']:,}")
                            row.cell(f"{rec['closing']:,}")
                            continue

                        else:
                            row = table.row()
                            row.cell(f"On {rec['date']} At {rec['time']}")
                            row.cell(f"{-rec['credit_or_debit']:,}")
                            row.cell("")
                            row.cell(f"{rec['closing']:,}")
                            continue

        pdf = PDF()
        pdf.add_page()  # According to the documentation of the fpdf2 library, this line automatically calls 'header' of the PDF class.
        pdf.output("Account_Statement.pdf")
