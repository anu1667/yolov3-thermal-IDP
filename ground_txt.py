import json


img_count = 8863

category = dict()

nopes = [8961, 8962, 8976, 8977, 8978, 9178, 9179, 9180, 9181, 9182, 9184, 9185, 9186, 9187, 9194, 9196, 9375, 9397, 9461, 9518]

with open('/home/anandita/Documents/acad/sem8/idp/categories_coco.txt' , 'r') as cat:
	count = 1
	for line in cat:
		category[count] = line.rstrip()
		count+=1

cat.close()

while(img_count <= 9545):

	if(img_count in nopes):
		pass

	else:
		with open('/home/anandita/MEGAsync Downloads/FLIR/FLIR_ADAS/validation/Annotations/FLIR_0' + str(img_count) + '.json' , 'r') as f:
			result = json.load(f)

			with open('/home/anandita/Documents/acad/sem8/idp/groundtruths_1/FLIR_0' + str(img_count) + '.txt' , 'w') as file:
				for item in result["annotation"]:		
					file.write(category[int(item["category_id"])] + ' ' + str(item['bbox'][0]) + ' ' + str(item['bbox'][1]) + ' ' + str(item['bbox'][2]) + ' ' + str(item['bbox'][3]) +'\n')


				file.close()
			
			f.close()

	img_count+=1
