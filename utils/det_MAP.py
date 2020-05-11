import json


with open("/home/anandita/darknet/results.json") as f:
	result = json.load(f)

	if len(result) > 0 and result[0] != None:
		count = 8863
		store = []
		# count_item = 0	
		for item in result:
			#count_item += 1
			filename = item["filename"]
			objects = item["objects"]

			#boxes = []

			if(len(objects) == 0):
				store.append(count)
				count+=1

			else:
				validclasses = ['person' , 'car' , 'bicycle']
				for i in range(len(objects)):
					class_name = objects[i]["name"].replace(' ' , '')
					center_x = objects[i]["relative_coordinates"]["center_x"]
					center_y = objects[i]["relative_coordinates"]["center_y"]
					width = objects[i]["relative_coordinates"]["width"]
					height = objects[i]["relative_coordinates"]["height"]
					confidence = objects[i]["confidence"]  

					top_x = center_x - (width/2.0) 
					top_y = center_y + (height/2.0)
					bottom_x = center_x + (width/2.0)
					bottom_y = center_y - (height/2.0)

					#boxes.append([top_x , top_y , bottom_x , bottom_y , class_name , confidence])

					with open("/home/anandita/Documents/acad/sem8/idp/detections_1/FLIR_0" + str(count) + ".txt" , 'a') as file:
						if class_name in validclasses:
							file.write(class_name + ' ' + str(confidence) + ' ' + str(top_x) + ' ' + str(top_y) + ' ' + str(width) + ' ' + str(height)  + '\n')

				file.close()
				count+=1

print(store)
		