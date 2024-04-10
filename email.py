class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Initialize an Email object with the provided email address, subject line, and email content.
        By default, the email is marked as unread.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    def mark_as_read(self):
        """Mark the email as read."""
        self.has_been_read = True
    
    inbox = []  # Class variable to store emails

    def populate_inbox(self):
        """
        Populate the inbox with sample emails.
        Each email is an instance of the Email class.
        """
        email1 = Email("hyperiondev@gmail.com", "Welcome", "Welcome to the platform!")
        email2 = Email("hyperiondev@yahoo.com", "Important Notice", "Please read this important notice.")
        email3 = Email("irokajuliet01@gmail.com", "Reminder", "Don't forget about our meeting tomorrow.")

        # Add the emails to the Inbox list
        self.inbox.append(email1)
        self.inbox.append(email2)
        self.inbox.append(email3)

    def list_emails(self):
        """List all emails in the inbox along with their subject lines."""
        for index, email in enumerate(self.inbox):
            print(f"{index}: {email.subject_line}")

    def read_email(self, email_index):
        """
        Read the email at the specified index in the inbox.
        If the index is valid, print the email details and mark it as read.
        """
        if 0 <= email_index < len(self.inbox):
            email = self.inbox[email_index]
            print(f"\nFrom: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print(f"Content: {email.email_content}")
            email.mark_as_read()
            print(f"Email marked as read: {email.subject_line}")
        else:
            print("Invalid email index.")

def main():
    """
    Main function to simulate an email application.
    Provides options to read emails, view unread emails, or quit the application.
    """
    email_simulator = Email("", "", "")
    email_simulator.populate_inbox()
    
    menu = True
    
    while True:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))
        if user_choice == 1:
            email_index = int(input("Enter the index of the email you want to read: "))
            email_simulator.read_email(email_index)
        elif user_choice == 2:
            print("\nUnread Emails:")
            for email in email_simulator.inbox:
                if not email.has_been_read:
                    print(f"Subject: {email.subject_line}")
        elif user_choice == 3:
            print("Quitting application...")
            break
        else:
            print("Oops - incorrect input.")

main()