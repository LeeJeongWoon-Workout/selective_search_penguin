img_copy=cv2.rectangle(img_copy,(gt_box[0],gt_box[1]),(gt_box[2],gt_box[3]),color=red,thickness=2)
iou_list=[]

for index,cand_box in enumerate(cand_rect):
  cand_box=list(cand_box)

  cand_box[2]+=cand_box[0]
  cand_box[3]+=cand_box[1]

  iou=compute_iou(cand_box,gt_box)
  iou_list.append((iou,cand_box))


NMS(iou_list,gt_box,img)
