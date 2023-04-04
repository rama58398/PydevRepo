import imaplib
import email

# connect to the email server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email_address', 'your_email_password')
mail.select('inbox')

# define the search pattern
search_pattern = 'Shaadi.com"'

# search for matching emails
result, data = mail.search(None, search_pattern)

# delete matching emails
if data[0]:
    email_ids = data[0].split()
    for email_id in email_ids:
        mail.store(email_id, '+FLAGS', '\\Deleted')
    mail.expunge()

# close the mailbox and logout
mail.close()
mail.logout()
