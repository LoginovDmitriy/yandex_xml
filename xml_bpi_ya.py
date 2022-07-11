import os
import xml.etree.ElementTree as et
import pymysql.cursors  
# import yadisk

# connection = pymysql.connect(host='Jino.ru MySQL:3306',
# 						user='9967724406_',
# 						password='Xedfr@123',
# 						db='bpi',
# 						charset='utf8mb4',
# 						cursorclass=pymysql.cursors.DictCursor)

# print ("connect successful!!")		

# connection = pymysql.connect(host='localhost',
# 					user='root',
# 					password='Xedfr@123',
# 					db='rent',
# 					charset='utf8mb4',
# 					cursorclass=pymysql.cursors.DictCursor)
# print ("connect successful!!")

# with connection.cursor() as cursor:
# 	sql = "SELECT * FROM flats"
# 	cursor.execute(sql)
	# c = cursor.fetchall()


# y = yadisk.YaDisk(token='AgAAAAAj8m5cAADLW0iNvma_LU_Ympdz11Xma-I')
# print(y.check_token())

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "data\\flats_rent.xml")

tree = et.parse(xml_file)

root = tree.getroot()

for i in range(len(c)):
	ids = c[i]['ids']
	adress = c[i]['adress']
	flat_type = c[i]['flat_type']
	area = c[i]['area']
	floor = c[i]['floor']
	total_f = c[i]['total_f']
	price = c[i]['price']
	creation_date = c[i]['creation_date']
	living_space = c[i]['living_space']
	description = c[i]['description']
	if flat_type == '1-комн. квартира':
		rooms = '1'
	elif flat_type == '2-комн. квартира':
		rooms = '2'
	elif flat_type == '3-комн. квартира':
		rooms = '3'		
	elif flat_type == '4-комн. квартира':
		rooms = '4'
	else:
		rooms = None

	new_object = et.SubElement(root, "offer", attrib={'internal-id': str(ids)})

	new_object_type = et.SubElement(new_object, 'type')
	new_object_type.text = 'аренда'

	new_object_property_type = et.SubElement(new_object, 'property-type')
	new_object_property_type.text = 'жилая'

	new_object_category = et.SubElement(new_object, 'category')
	new_object_category.text = 'квартира'

	new_object_creation_date = et.SubElement(new_object, 'creation-date')
	new_object_creation_date.text = creation_date

	new_object_location = et.SubElement(new_object, 'location')
	new_object_location_country = et.SubElement(new_object_location, 'country')
	new_object_location_country.text = 'Россия'

	new_object_location_locality_name = et.SubElement(new_object_location, 'locality-name')
	new_object_location_locality_name.text = 'Санкт-Петербург'
	new_object_location_adress = et.SubElement(new_object_location, 'address')
	new_object_location_adress.text = adress


	new_object_sales_agent = et.SubElement(new_object, 'sales-agent')
	new_object_sales_agent_name = et.SubElement(new_object_sales_agent, 'name')
	new_object_sales_agent_name.text = 'Дмитрий'
	new_object_sales_agent_phone = et.SubElement(new_object_sales_agent, 'phone')
	new_object_sales_agent_phone.text = '+79956078005'	
	new_object_sales_agent_category = et.SubElement(new_object_sales_agent, 'category')
	new_object_sales_agent_category.text = 'агентство'


	new_object_price = et.SubElement(new_object, 'price')
	new_object_price_value = et.SubElement(new_object_price, 'value')
	new_object_price_value.text = price
	new_object_price_currency = et.SubElement(new_object_price, 'currency')
	new_object_price_currency.text = 'RUR'


	new_object_prepayment = et.SubElement(new_object, 'prepayment')
	new_object_prepayment.text = '100'

	new_object_agent_fee = et.SubElement(new_object, 'agent-fee')
	new_object_agent_fee.text = '50'	

	new_object_utilities_included = et.SubElement(new_object, 'utilities-included')
	new_object_utilities_included.text = 'нет'


	new_object_area = et.SubElement(new_object, 'area')
	new_object_area_value = et.SubElement(new_object_area, 'value')
	new_object_area_value.text = area
	new_object_area_unit = et.SubElement(new_object_area, 'unit')
	new_object_area_unit.text = 'кв.м.'	
	
	new_object_living_space = et.SubElement(new_object, 'living-space')
	new_object_living_space_value = et.SubElement(new_object_living_space, 'value')
	new_object_living_space_value.text = living_space
	new_object_livind_space_unit = et.SubElement(new_object_living_space, 'unit')
	new_object_livind_space_unit.text = 'кв.м.'	


	l = os.listdir('C:\\Python37\\RENT\\'+str(ids)+'\\')
	number = len(l)
	# y.mkdir('/RENT/'+str(ids))
	# y.publish('/RENT/'+str(ids))
	for i in range(number-1):
		new_object_image = et.SubElement(new_object, 'image')
		# with open('C:\\Python37\\RENT\\'+str(ids)+'\\' + str(i+1) + '.jpg', 'rb') as f:
		# 	y.upload(f, '/RENT/'+str(ids)+'/'+str(i+1)+'.jpg')
		# 	y.publish('/RENT/'+str(ids)+'/'+str(i+1)+'.jpg')
		r = 'http://9967724406.myjino.ru/RENT/'+str(ids)+'/'+str(i+1)+'.jpg'
		new_object_image.text = r


	new_object_renovation = et.SubElement(new_object, 'renovation')
	new_object_renovation.text = 'евроремонт'

	new_object_description = et.SubElement(new_object, 'description')
	new_object_description.text = description

	if flat_type != 'Квартира-студия':
		new_object_rooms = et.SubElement(new_object, 'rooms')
		new_object_rooms.text = rooms
		new_object_rooms_offered = et.SubElement(new_object, 'rooms-offered')
		new_object_rooms_offered.text = rooms


	new_object_floor = et.SubElement(new_object, 'floor')
	new_object_floor.text = floor

	if flat_type == 'Квартира-студия':
		new_object_studio = et.SubElement(new_object, 'studio')
		new_object_studio.text = 'да'


	new_object_floors_total = et.SubElement(new_object, 'floors-total')
	new_object_floors_total.text = total_f

	print('Объявление - ' + ids + ' загружено.')






	# new_object_contact = et.SubElement(new_object, 'contact')
	# new_object_contact_name = et.SubElement(new_object_contact, 'name')
	# new_object_contact_telephone = et.SubElement(new_object_contact, 'telephone')
	# new_object_contact_email = et.SubElement(new_object_contact, 'email')

	# new_object_category = et.SubElement(new_object, 'category')
	# new_object_theme = et.SubElement(new_object, 'theme')
	# new_object_description = et.SubElement(new_object, 'description')

	# new_object_price = et.SubElement(new_object, 'price')
	# new_object_price_value = et.SubElement(new_object_price, 'value')

	# new_object_location = et.SubElement(new_object, 'location')
	# new_object_location_country = et.SubElement(new_object_location, 'country')
	# new_object_location_oblast = et.SubElement(new_object_location, 'oblast')
	# new_object_location_city = et.SubElement(new_object_location, 'city')
	# new_object_location_street = et.SubElement(new_object_location, 'street')
	# new_object_location_house = et.SubElement(new_object_location, 'house')

	# new_object_square = et.SubElement(new_object, 'square')
	# new_object_square_total = et.SubElement(new_object_square, 'total')
	# # new_object_square_kitchen = et.SubElement(new_object_square, 'kitchen')

	# new_object_parameters = et.SubElement(new_object, 'parameters')
	# new_object_parameters_story = et.SubElement(new_object_parameters, 'story')
	# new_object_parameters_story_count = et.SubElement(new_object_parameters, 'story_count')
	# new_object_parameters_rooms = et.SubElement(new_object_parameters, 'rooms')
	# new_object_parameters_repairs = et.SubElement(new_object_parameters, 'repairs')
	# new_object_parameters_ipoteka = et.SubElement(new_object_parameters, 'ipoteka')
	# new_object_parameters_status_flat = et.SubElement(new_object_parameters, 'status_flat')
	# new_object_parameters_studio = et.SubElement(new_object_parameters, 'studio')
	# new_object_parameters_apartament = et.SubElement(new_object_parameters, 'apartament')

	# new_object_images = et.SubElement(new_object, 'images')
	# # new_object_images_image = et.SubElement(new_object_images, 'image')
	# l = os.listdir('C:\\Python37\\BPI\\'+str(ids)+'\\')
	# number = len(l)
	# y.mkdir('/BPI/'+str(ids))
	# y.publish('/BPI/'+str(ids))
	# for i in range(number-1):
	# 	with open('C:\\Python37\\BPI\\'+str(ids)+'\\' + str(i+1) + '.jpg', 'rb') as f:
	# 		y.upload(f, '/BPI/'+str(ids)+'/'+str(i+1)+'.jpg')
	# 		y.publish('/BPI/'+str(ids)+'/'+str(i+1)+'.jpg')
	# 		r = y.get_meta('/BPI/'+str(ids)+'/'+str(i+1)+'.jpg').public_url
	# 		new_object_images_image = et.SubElement(new_object_images, 'image')
	# 		new_object_images_image.text = r

	# new_object_afynewbuilding = et.SubElement(new_object, 'afynewbuilding')



	# new_object_contact_name.text = 'Дмитрий'
	# new_object_contact_telephone.text = '+7(969)707-49-51'
	# new_object_contact_email.text = 'loginovd@list.ru'

	# new_object_category.text = '175'
	# new_object_theme.text = 'Продажа квартиры в ЖК Чистое Небо'
	# new_object_description.text = 'Продается отличная квартира по переуступке. ЖК Чистое Небо от застрйзика SetlCity.'

	# new_object_price_value.text = price

	# new_object_location_country.text = 'Россия'
	# new_object_location_oblast.text = 'Санкт-Петербург'
	# new_object_location_city.text = 'Санкт-Петербург'
	# if och == '4':
	# 	street = 'Плесецкая ул.'
	# 	house = '20к1'
	# elif och == '5':
	# 	street = 'Комендантский пр.'
	# 	house = '66к1'
	# elif och == '6':
	# 	street = 'Комендантский пр.'
	# 	house = 'стр.6'
	# elif och == '7':
	# 	street = 'Комендантский пр.'
	# 	house = 'стр.7.6'
	# new_object_location_street.text = street
	# new_object_location_house.text = house

	# new_object_square_total.text = area
	# # new_object_square_kitchen.text = '0'

	# new_object_afynewbuilding.text = '1'

	# new_object_parameters_story.text = floor
	# new_object_parameters_story_count.text = total_f
	# new_object_parameters_rooms.text = flat_type
	# new_object_parameters_repairs.text = '1'
	# new_object_parameters_ipoteka.text = 'y'
	# new_object_parameters_status_flat.text = '3'
	# new_object_parameters_studio.text = 'y'
	# new_object_parameters_apartament.text = 

# handle = tree.toprettyxml(root, pretty_print=True, encoding='utf-8', xml_declaration=True)
# tree.writelines(handle)

tree.write(xml_file, encoding="UTF-8", xml_declaration=True)