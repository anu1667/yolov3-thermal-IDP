import json
from matplotlib import pyplot
from matplotlib.patches import Rectangle


with open("/home/anandita/darknet/result4.json") as f:
	result = json.load(f)

	if len(result) > 0 and result[0] != None:
		count = 10000
		#skip = []
		#keep = []
		for item in result:
			filename = item["filename"]
			objects = item["objects"]

			boxes = []

			#keep.append(filename)
			for i in range(len(objects)):
				class_name = objects[i]["name"]
				center_x = objects[i]["relative_coordinates"]["center_x"] * 640
				center_y = objects[i]["relative_coordinates"]["center_y"] * 512
				width = objects[i]["relative_coordinates"]["width"] * 640
				height = objects[i]["relative_coordinates"]["height"] * 512
				confidence = objects[i]["confidence"] * 100

				top_x = center_x - (width/2.0)
				top_y = center_y + (height/2.0)
				bottom_x = center_x + (width/2.0)
				bottom_y = center_y - (height/2.0)

				boxes.append([top_x , top_y , bottom_x , bottom_y , class_name , confidence])

			# load the image
			data = pyplot.imread(filename)
			
			# plot the image
			pyplot.imshow(data , cmap ='gray')
	
			# get the context for drawing boxes
			ax = pyplot.gca()
			
			# plot each box
			for i in range(len(boxes)):
				box = boxes[i]
				# get coordinates
				x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
				# calculate width and height of the box
				w, h = x2 - x1, y2 - y1
				# draw text and score in top left corner
				#label = "%s (%.3f)" % (box[4], box[5])
				label = "%s" %box[4]
				if(label == 'person'):
					# create the shape
					rect = Rectangle((x1, y1), w, h, fill=False, color='Blue' , lw = 1.5)
					# draw the box
					ax.add_patch(rect)
					pyplot.text(x1, y1, label, color='Blue')
				elif(label == 'car'):
					# create the shape
					rect = Rectangle((x1, y1), w, h, fill=False, color='Green' , lw = 1.5)
					# draw the box
					ax.add_patch(rect)	
					pyplot.text(x1, y1, label, color='Green')
				elif(label == 'bicycle'):
					# create the shape
					rect = Rectangle((x1, y1), w, h, fill=False, color='Yellow' , lw = 1.5)
					# draw the box
					ax.add_patch(rect)	
					pyplot.text(x1, y1, label, color='Yellow')
				else:
					pass

				#pyplot.pause(0.01)
				
			# show the plot
			pyplot.gca().set_axis_off()
			pyplot.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
			pyplot.margins(0,0)
			pyplot.gca().xaxis.set_major_locator(pyplot.NullLocator())
			pyplot.gca().yaxis.set_major_locator(pyplot.NullLocator())
			pyplot.savefig('/home/anandita/Documents/acad/sem8/idp/results_2/result_' + str(count) + '.jpeg', bbox_inches='tight' , pad_inches = 0)
			ax.clear()
			count+=1
					

# print(total)
#print(keep)







