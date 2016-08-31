class Contact(object):
	def __init__(self, first_name, last_name, mobile_number = "", work_number= "", email = ""): 
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.mobile_number = mobile_number
		self.work_number = work_number

	def send_text(self, message):
		if self.mobile_number != "":
			print "To: %s - %s" % (self.mobile_number, message)
		else: 
			print "Error, no mobile number provided"

def main():
	contact_list = []

	contact_jim = Contact("Jim", "Moore")
	contact_amy = Contact("Amy", "Fire", "777-777-7777")
	contact_tony = Contact("Tony", "Soprano", "111-111-1111", "333-333-3333", "tony.pizza@gmail.com")

	contact_list.append(contact_jim)
	contact_list.append(contact_amy)
	contact_list.append(contact_tony)

	for info in contact_list:
		print info.first_name
		print info.last_name
		print info.email
		print info.mobile_number
		print info.work_number

	for info in contact_list:
		info.send_text("Hello everyone!")





if __name__ == "__main__": 
	main()
