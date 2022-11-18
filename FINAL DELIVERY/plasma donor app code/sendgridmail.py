# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
#
# def sendmail(usermail,subject,content):
#     message = Mail(from_email='cse19.rebison@petengg.ac.in',to_emails=usermail,subject=subject,html_content='<strong> {} </strong>'.format(content))
#     try:
#         sg = SendGridAPIClient("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")
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e)