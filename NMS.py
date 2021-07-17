def NMS(iou_list,gt_box,img):
  img_copy=img.copy()
  iou_list=max(iou_list)
  iou_list_loc=iou_list[1]
  cv2.rectangle(img_copy,(iou_list_loc[0],iou_list_loc[1]),(iou_list_loc[2],iou_list_loc[3]),green,thickness=1)
  cv2.rectangle(img_copy,(gt_box[0],gt_box[1]),(gt_box[2],gt_box[3]),red,thickness=2)
  text="{:} : {:.2f}".format("iou",iou_list[0])
  cv2.putText(img_copy,text,(gt_box[0]+100,gt_box[1]+10),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.4,color=(0,255,0),thickness=1)
  plt.figure(figsize=(8,8))
  plt.imshow(img_copy)
  plt.show()
