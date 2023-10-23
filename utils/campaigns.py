import pandas as pd
from utils.twilio_helper import send_twilio_message, send_twilio_photo
import time

def ret_camp(product,name):

       return campgn[product].format(name=name),links[product]



campgn={'HL':'''
🏡 Home Loan Special Offer! 🏡

Dear {name},

Are you dreaming of owning your own home? We're here to make that dream come true! At IDFC BANK, we have an exclusive limited-time offer just for you.

✨ Our Home Loan Special Features:
🔑 Low Interest Rates
💰 Flexible Repayment Options
📋 Quick and Easy Approval Process
🎁 Special Discounts for First-Time Homebuyers

Don't miss out on this fantastic opportunity to secure the home of your dreams. Take the first step towards homeownership today!

💬 Reply with "Home" to get more information about our home loan options or to speak to one of our loan experts.

📞 You can also call us at [Your Contact Number] for immediate assistance.

🕐 Act now, and turn your homeownership dream into a reality! 🏡

https://www.idfcfirstbank.com/personal-banking/loans/home-loan

Best regards,
Suyash Dongare
Sr. Loan Officer
IDFC FIRST BANK
''',

'VH':'''🚗 Car Loan Special Offer! 🚗

Dear {name},

Is owning a brand new car in your future? We're here to help you make it happen! At IDFC FIRST BANK we're excited to introduce our exclusive limited-time offer just for you.

✨ Our Car Loan Special Features:
🔑 Competitive Interest Rates
💰 Affordable Monthly Payments
📋 Quick and Easy Approval Process
🚀 Fast Access to Your Dream Car

Don't miss out on this amazing opportunity to drive away with your dream car. Start your journey towards car ownership today!

💬 Reply with "Car" to learn more about our car loan options or to speak with one of our loan experts.

📞 You can also call us at 9822155190 for immediate assistance.

🕐 Act now, and make your dream car a reality! 🚗

https://www.idfcfirstbank.com/personal-banking/loans/car-loan

Best regards,
Suyash Dongare
Sr. Loan Officer
IDFC FIRST BANK
''',

'TL':'''🏍️ Two-Wheeler Loan Special Offer! 🏍️

Dear {name},

Ready to hit the road on a brand new two-wheeler? We're here to help you make it happen! At IDFC FIRST BANK, we're thrilled to introduce our exclusive limited-time offer just for you.

✨ Our Two-Wheeler Loan Special Features:
🔑 Low-Interest Rates
💰 Affordable Monthly Payments
📋 Quick and Easy Approval Process
🛵 Fast Access to Your Dream Ride

Don't miss out on this fantastic opportunity to own the two-wheeler of your dreams. Start your journey towards easy, convenient, and affordable transportation today!

💬 Reply with "Two-Wheeler" to learn more about our two-wheeler loan options or to speak with one of our loan experts.

📞 You can also call us at 9822155190 for immediate assistance.

🕐 Act now and hit the road in style! 🏍️

https://www.idfcfirstbank.com/personal-banking/loans/two-wheeler-loan

Best regards,
Suyash Dongare
Sr. Loan Officer
IDFC FIRST BANK
'''}

links={'HL':'https://i.ibb.co/ZGLCJV9/idfc-first-bank-home-loan.png',
       'TL':'https://i.ibb.co/5s8x8PQ/idfc-first-bank-bike-loan.jpg',
       'VH':'https://i.ibb.co/YXBK53m/idfc-first-bank-car-loan.jpg'}


df = pd.read_excel('D:\whatsapp_bot\list.xlsx')
def run_campaign():
       for index, row in df.iterrows():
              # print(row['Mobile number'])
              to = 'whatsapp:'+str(row['Mobile number'])
              name = row['Name ']
              product = row['Product']
              message, link = ret_camp(product, name)
              send_twilio_photo(message, to, link)
              time.sleep(3)

       return None




if __name__=='__main__':
       run_campaign()


