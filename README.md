# Global Banking Services
####
### Banking Services Demo Program
#### This program simulates a simple banking system, offering the following features:

* **Account Creation**: Users can create a new bank account by providing personal details. My Program will automatically generate a unique account number for each new account. The initial balance for every new account is set to ₹1000.

* **Account Login**: Once an account is created, users can log in by entering their unique account number and the password they set during account creation.

* **Deposite and Withdrawal**: After logging in, customers can deposit money into their account and withdraw funds as needed. The program tracks account balances in real-time.

* **Account Statement**: Users can generate an account statement (in PDF format) displaying up to the last 20 transactions for their account.

This demo program aims to showcase basic banking functionalities, such as account management, balance handling, and transaction history tracking.

### Key features in summary:

* Account Creation with Unique Account Number
* Login using Account Number & Password
* Deposit and Withdrawal Capabilities
* Account Statement (PDF) Generation for Transaction History

<br>

> **ⓘ&nbsp;**
> Once the Binder server has loaded, click on the **Terminal** option in the menu. This will open a terminal window within the Binder interface. In the terminal, follow the usage guide provided below to run the program.

### Usage Guide

### 1. Prerequisites

Before you run the program, make sure you have following installed in your machine.

You can install the required dependencies using pip:

```
bash

$ pip install -r requirements.txt
```

### 2. Run the Program

To start the banking system, run the main program:

```
bash

$ python main.py
```

### 3. Creating a New Account

Once the program is running, follow these steps to create a new bank account:

1.&nbsp; Choose the option to Create a New Account. <br>
2.&nbsp; Provide the required personal details, such as your name and contact.<br>
3.&nbsp; The program will automatically generate a unique account number for your new account.<br>
4.&nbsp; Set a password for your account to ensure secure access.
Your initial balance will be ₹1000.

> **ⓘ&nbsp; Forgot Account Number or Password?**
> &nbsp; If you've forgotten your account number or password, you can check the `input_data1.csv` file. This file contains all the user data, including the account number and password you used to register.




### 4. Logging Into Your Account

To log into your account:

1.&nbsp; Select the Account Login option.<br>
2.&nbsp; Enter your account number and the password you created during account registration.<br>
3.&nbsp; Once logged in, you'll have access to your account's features (deposit, withdrawal, and account statement).


### 5. Depositing Money

After logging in, you can deposit money into your account:

1.&nbsp; Select the Deposit Money option from the menu.<br>
2.&nbsp; Enter the amount you'd like to deposit.<br>
3.&nbsp; The program will update your account balance accordingly.

### 6. Withdrawing Money

To withdraw money from your account:

1.&nbsp; Select the Withdraw Money option.<br>
2.&nbsp; Enter the amount you'd like to withdraw (ensure your balance is sufficient).<br>
3.&nbsp; The program will update your balance after the withdrawal.


### 7. Generating Account Statement

To generate an account statement:

1.&nbsp; Choose the Account Statement option.<br>
2.&nbsp; The program will generate a PDF of the last 20 transactions on your account.<br>
3.&nbsp; The statement will be saved in the current directory.


### 8. Exiting the Program

When you're done using the banking system, you can exit the program by selecting the Logout option from the menu.