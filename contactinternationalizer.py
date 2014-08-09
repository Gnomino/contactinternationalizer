import csv
import io
import phonenumbers
import codecs
with codecs.open('google.csv', 'r', encoding="utf-16le") as f:
  t = f.read()

r = csv.reader(io.StringIO(t))
w = csv.writer(open('contacts.out', 'w+', newline=''))
headings = r.__next__()
w.writerow(headings)
phone1 = headings.index('Phone 1 - Value')
phone2 = headings.index('Phone 2 - Value')
for i in r:
	if len(i[phone1]) > 0:
		splitted = i[phone1].split(' ::: ')
		nbs = []
		for p in splitted:
			p = phonenumbers.parse(p, "FR")
			p = phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
			nbs.append(p)
		i[phone1] = ' ::: '.join(nbs)
	if len(i[phone2]) > 0:
		splitted = i[phone2].split(' ::: ')
		nbs = []
		for p in splitted:
			p = phonenumbers.parse(p, "FR")
			p = phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
			nbs.append(p)
		i[phone2] = ' ::: '.join(nbs)
	w.writerow(i)