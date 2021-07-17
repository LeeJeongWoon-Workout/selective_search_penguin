gt_box=[35,45,130,175]
_,regions=selectivesearch.selective_search(img,scale=10,min_size=2000)
cand_rect=[cand['rect'] for cand in regions]
imt_copy=img.copy()
green=(0,255,0)
red=(255,0,0)
img_copy=img.copy(
