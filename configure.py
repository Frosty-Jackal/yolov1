Data_num = 2975
batch_size=1
epoch=15
print_freq=100
train_freq=3
iou_thresh=0.5
cls_num=8
bound_confidence=0.35

url="http://127.0.0.1:5000/"
COLOR = [(255,0,0),(255,125,0),(255,255,0),(255,0,125),(255,0,250),
         (255,125,125),(255,125,250),(125,125,0),(0,255,125),(255,0,0),
         (0,0,255),(125,0,255),(0,125,255),(0,255,255),(125,125,255),
         (0,255,0),(125,255,125),(255,255,255),(100,100,100),(0,0,0),]  # 用来标识20个类别的bbox颜色，可自行设定

GL_CLASSES =['car', 'person', 'rider', 'truck', 'bus', 'train', 'motorcycle', 'bicycle'] 
