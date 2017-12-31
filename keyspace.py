# Simple key space calculator

passwd = raw_input('Password? ')
length = len(passwd)
symbolset = "!\"#$%&'()*+,-./:;<=>?@[\]^_\\`{|}~"
charcount = 0
symsum = 0
powerlength = False

uppercase = sum(1 for x in passwd if x.isupper())
lowercase = sum(1 for x in passwd if x.islower())
stringdigit = sum(1 for x in passwd if x.isdigit())

for syms in symbolset:
    if syms in passwd:
        symsum = len(syms)

print 'Uppercase letters:', uppercase
print 'Lowercase letters:', lowercase
print 'Digits in password:', stringdigit
print 'Symbols in password:', symsum

if uppercase >= 1:
    charcount = charcount + 26
if lowercase >= 1:
    charcount = charcount + 26
if stringdigit >= 1:
    charcount = charcount + 10
if symsum >= 1:
    charcount = charcount + 32

print 'Length:', length

if length < 14:
    print 'PASSWORD LESS THAN RECOMMENDED 14 CHARACTERS!'
else:
    print 'LENGTH OK.'
    powerlength = True

key = (charcount ** length)
print 'Keyspace: ', "{:,}".format(key)

if powerlength is True:
    print '... zomg the possibilities are endless!!'