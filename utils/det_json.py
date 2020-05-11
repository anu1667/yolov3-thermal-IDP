import json 
import os

data_list = []


with open("/home/anandita/darknet/results.json") as f:
	result = json.load(f)

	if len(result) > 0 and result[0] != None:
		for item in result:
			filename = os.path.basename(item["filename"])
			objects = item["objects"]

			for i in range(len(objects)):
				image_dict = {}
				category_id = objects[i]["class_id"] + 1
				center_x = objects[i]["relative_coordinates"]["center_x"] * 640
				center_y = objects[i]["relative_coordinates"]["center_y"] * 512
				width = objects[i]["relative_coordinates"]["width"] * 640
				height = objects[i]["relative_coordinates"]["height"] * 512
				confidence = objects[i]["confidence"]

				top_x = center_x - (width/2.0)
				top_y = center_y + (height/2.0)
				bottom_x = center_x + (width/2.0)
				bottom_y = center_y - (height/2.0)

				w = round(abs(bottom_x - top_x))
				h = round(abs(top_y - bottom_y))
				image_dict["image_id"] = int(filename[6:10])
				image_dict["category_id"] = int(category_id)
				image_dict["bbox"] = [round(top_x) , round(top_y) , w ,h]
				image_dict["score"] = confidence

				data_list.append(image_dict)


with open('pred.json', 'w') as outfile:
    json.dump(data_list, outfile)

	


