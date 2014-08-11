import sys
import getopt
import smtplib
from datetime import date


def get_subject():
    # i.e. Sunday, August 10
    today = date.today()
    return today.strftime("What'd you get done today? %A, %B %d")


def done(username, password, email, cal, msg):
    fromaddress = email
    toaddress  = '%s@team.idonethis.com' % cal
    subject = get_subject()
    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromaddress, toaddress, subject, msg)

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddress, [toaddress], message)
        server.quit()
    except Exception as e:
        print 'Error sending message: %s' % e


def main(argv):
    cal = None
    email = None
    password = None
    text = None

    try:
        opts, args = getopt.getopt(argv,"hc:e:p:t:",["cal=","email=","password=","text="])
    except getopt.GetoptError as e:
        print 'Error with getopt: %s' % e
        print 'idonethis.py -c <cal> -e <email> -p <password> -t <text>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'idonethis.py -g <generations> -c <crossover-rate> -m <mutation-rate> -s <population-size> -p <parameters> -f <input-file>'
            sys.exit()
        elif opt in ("-c", "--cal"):
            cal = arg
        elif opt in ("-e", "--email"):
            email = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-t", "--text"):
            text = arg

    if (not cal) or (not email) or (not password) or (not text):
        print 'Missing option parameter, see usage:'
        print 'idonethis.py -c <cal> -e <email> -p <password> -t <text>'
        sys.exit(2)

    if '@gmail.com' not in email and '@' in email:
        print 'Email not supported, yet. Only email service supported is gmail.'
        sys.exit(2)

    if (not cal) or (not email) or (not password) or (not text):
        print 'Missing option parameter, see usage:'
        print 'idonethis.py -c <cal> -e <email> -p <password> -t <text>'
        sys.exit(2)

    username = email[:email.index('@')]
    done(username, password, email, cal, text)


if __name__ == "__main__":
    main(sys.argv[1:])
