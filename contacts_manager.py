import contact 

contact_list = []

def show_current_contacts():
	print contact_list


def add_new_contact(first_name1, last_name1, mobile_number1 = "", work_number1 = "", email1 = ""):
	first_name1 = first_name1.upper().strip()
	last_name1 = last_name1.upper().strip()
	email1 = email1.upper().strip()

	
	if not contact_list:
		print "Contact added to empty list" 
		new_contact = contact.Contact(first_name = first_name1, last_name = last_name1, mobile_number = mobile_number1, work_number = work_number1, email = email1)
		contact_list.append(new_contact)
		return 
	else:
		for info in contact_list:
			print info.first_name, info.last_name, "iterating" 
	 		if first_name1 == info.first_name and last_name1 == info.last_name:
				print "Error, that contact already is in your contact list"
				return 
			else: 
				print "No matches found, adding a new contact", first_name1, last_name1
				new_contact = contact.Contact(first_name = first_name1, last_name = last_name1, mobile_number = mobile_number1, work_number = work_number1, email = email1)
				contact_list.append(new_contact)
				return
	


def edit_existing_contact(current_first_name, current_last_name, new_first_name = "", new_last_name = "", new_mobile_number = "", new_work_number = "", new_email = ""):
	new_first_name = new_first_name.upper().strip()
	new_last_name = new_last_name.upper().strip()
	new_email = new_email.upper().strip()

	for info in contact_list:
		print info.first_name, info.last_name, "iterating" 
		
		if current_first_name == info.first_name and current_last_name == info.last_name:
			#changing the first name 
			if new_first_name != "":
				info.first_name = new_first_name
			#changing the last name 
			if new_last_name != "":
				info.last_name = new_last_name
			#changing the mobile number 
			if new_mobile_number != "":	
				info.mobile_number = new_mobile_number
			#changin the work number 
			if new_work_number != "":
				info.work_number = new_work_number
			#changing the email 
			if new_email != "":
				info.email = new_email


		else: 
			print "Error that contact does not exist"



# def delete_existing_contact():


# def exit_program():





def main():

	add_new_contact('jane', 'doe', '555-555-5555', '666-666-666', 'jane@gmail.com')
	add_new_contact('mike', 'doe', '555-555-5555', '666-666-666', 'mike@gmail.com')

	edit_existing_contact('mike', 'doe', new_first_name = 'jim')


	for info in contact_list:
		print info.first_name
		print info.last_name
		print info.email
		print info.mobile_number
		print info.work_number




if __name__ == "__main__": 
	main()