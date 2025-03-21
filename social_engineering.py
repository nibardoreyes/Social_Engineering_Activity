###############################################################################
# Dev:      Jesse Turner, Keelia Mattison, and Alejandro Barranco, Nibardo Reyes Felix
# Class:    CYB-420: Global Perspectives on Cyber Warfare
# Version:  V1
###############################################################################
import random

def phishing_email():
    emails = [
        {"sender": "support@civilstructgeo.org", "subject": "Urgent: Your Account is Compromised!", "body": "Dear User, We've detected unusual activity on your account. Please confirm your identity by clicking this link: http://verify-now.civilstructgeo.org. Failure to do so may result in account suspension.", "correct": "Report"},
        {"sender": "admin@aerofluidthermo.org", "subject": "Claim Your Free Gift Now!", "body": "Congratulations! You've been selected for an exclusive prize. Click the link below to claim your reward: http://getprize.aerofluidthermo.org", "correct": "Report"},
        {"sender": "billing@civilstructgeo.org", "subject": "Final Notice: Payment Overdue", "body": "Your last invoice remains unpaid. Please settle immediately via this link: http://paynow.civilstructgeo.org to avoid service disruption.", "correct": "Report"},
        {"sender": "it-support@aerofluidthermo.org", "subject": "Password Reset Required", "body": "Your email password has expired. Click here to reset it now: http://resetpassword.aerofluidthermo.org", "correct": "Report"},
        {"sender": "security@civilstructgeo.org", "subject": "Security Alert: New Login Attempt", "body": "We noticed a login attempt from a new location. If this wasn't you, verify your identity here: http://securelogin.civilstructgeo.org", "correct": "Report"},
        {"sender": "helpdesk@aerofluidthermo.org", "subject": "You Have a New Voicemail", "body": "You missed a voicemail. Click here to listen: http://voicemail.aerofluidthermo.org", "correct": "Report"},
        {"sender": "promo@civilstructgeo.org", "subject": "Exclusive Deal Just for You!", "body": "Get 50% off on your next purchase! Claim your coupon here: http://exclusive-deal.civilstructgeo.org", "correct": "Report"},
        {"sender": "survey@aerofluidthermo.org", "subject": "Complete a Survey and Win!", "body": "Participate in our quick survey and win amazing prizes! Click here: http://survey-rewards.aerofluidthermo.org", "correct": "Report"},
        {"sender": "alert@civilstructgeo.org", "subject": "Bank Account Locked", "body": "Your bank account is locked due to suspicious activity. Verify your identity immediately: http://bank-verify.civilstructgeo.org", "correct": "Report"},
        {"sender": "lottery@aerofluidthermo.org", "subject": "You've Won a Lottery!", "body": "Congratulations! You've won $500,000! Claim now: http://lotterywin.aerofluidthermo.org", "correct": "Report"}
    ]
    return random.sample(emails, 5)

def legitimate_email():
    emails = [
        {"sender": "hr@yourcompany.com", "subject": "Reminder: Team Meeting Tomorrow", "body": "Hello Team, Just a reminder that we have a team meeting scheduled for tomorrow at 10 AM. See you all there!", "correct": "Respond"},
        {"sender": "support@banking-secure.com", "subject": "Account Security Notification", "body": "As part of our routine security measures, we wanted to notify you of recent changes to your account. If this wasn’t you, please contact our official support line immediately.", "correct": "Respond"},
        {"sender": "manager@company.com", "subject": "Project Deadline Update", "body": "The deadline for the current project has been extended by one week. Let’s discuss further in our next meeting.", "correct": "Respond"},
        {"sender": "admin@healthcareprovider.com", "subject": "Upcoming Appointment Confirmation", "body": "Your appointment is scheduled for next Monday at 3 PM. Please confirm your availability.", "correct": "Respond"},
        {"sender": "support@techservice.com", "subject": "Technical Assistance Request", "body": "We have received your technical support request and will be following up shortly.", "correct": "Respond"},
        {"sender": "travel@airlines.com", "subject": "Flight Itinerary Update", "body": "Your flight details have changed. Please review the updated itinerary.", "correct": "Respond"},
        {"sender": "info@conference2024.com", "subject": "Conference Registration Successful", "body": "Thank you for registering for the 2024 Tech Conference. More details will be shared soon.", "correct": "Respond"},
        {"sender": "help@ecommerce.com", "subject": "Order Shipped Notification", "body": "Your recent order has been shipped and is expected to arrive within 3 days.", "correct": "Respond"},
        {"sender": "university@edu.com", "subject": "Course Enrollment Confirmation", "body": "You have successfully enrolled in the upcoming course. Further instructions will follow.", "correct": "Respond"},
        {"sender": "updates@newslettersite.com", "subject": "Weekly Newsletter", "body": "Check out the latest news and updates in this week’s edition of our newsletter.", "correct": "Respond"}
    ]
    return random.sample(emails, 5)

def generate_quiz():
    phishing_emails = phishing_email()
    legitimate_emails = legitimate_email()
    questions = phishing_emails + legitimate_emails
    random.shuffle(questions)
    score = 0

    for i, email in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(f"From: {email['sender']}")
        print(f"Subject: {email['subject']}")
        print(f"Body: {email['body']}")
        print("\nWould you like to: \n1. Report \n2. Respond")
        
        choice = input("Enter 1 or 2: ").strip()
        user_choice = "Report" if choice == "1" else "Respond"
        
        if user_choice == email['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct action was: {email['correct']}")

    print(f"\nFinal Score: {score}/10")

if __name__ == "__main__":
    generate_quiz()
