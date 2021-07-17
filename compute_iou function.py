def compute_iou(c_box,g_box):
  x1=np.maximum(c_box[0],g_box[0])
  y1=np.maximum(c_box[1],g_box[1])
  x2=np.minimum(c_box[2],g_box[2])
  y2=np.minimum(c_box[3],g_box[3])

  intersection=np.maximum(x2-x1,0)*np.maximum(y2-y1,0)
  c_area=(c_box[2]-c_box[0])*(c_box[3]-c_box[1])
  g_area=(g_box[2]-g_box[0])*(g_box[3]-g_box[1])

  union=c_area+g_area-intersection

  return intersection/union
