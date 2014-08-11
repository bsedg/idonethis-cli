import sys
import getopt

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

if __name__ == "__main__":
    main(sys.argv[1:])
