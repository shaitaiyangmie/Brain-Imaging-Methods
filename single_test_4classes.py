import os
import torch
from torch.utils.data import DataLoader, Dataset
import cv2.cv2 as cv2
from torchvision import models, transforms
import torch.nn as nn
import numpy as np

test_cate = '/Users/shaotianyu01/Desktop/school/11.4/test_new'
# test_root = '/Users/shaotianyu01/Desktop/school/11.4/test_new/jiao/cut_jiao_20.jpg.jpg'
test_root = '/Users/shaotianyu01/Desktop/school/img_pred/cut.jpg'
# test_root = '/Users/shaotianyu01/Desktop/school/img_pred/'
# list_name = os.listdir(test_root)
# for name in list_name:
#     if '.jpg' in name:
#         test_root = os.path.join(test_root, name)
#         break
cate2label = {}
label2cate_orig = {}
label2cate = {0: 'lin', 1: 'xue', 2: 'jiao', 3: 'jia'}
list_img = []
list_dir = []
list_label = []
list_cate = os.listdir(test_cate)
list_cate = [cur for cur in list_cate if cur != '.DS_Store']

img = cv2.imread(test_root)
img = cv2.resize(img, (128, 128))
list_img.append(img)


class Mydata(Dataset):
    def __init__(self, x):
        self.X = x
        self.as_tensor = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.625, 0.448, 0.688], [0.131, 0.177, 0.101]),
        ])

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x_idx = self.X[idx]
        x_idx = self.as_tensor(x_idx)
        x_idx = x_idx.type(torch.FloatTensor)
        return x_idx


test_set = Mydata(list_img)
test_loader = DataLoader(
    test_set,
    batch_size=1,
    shuffle=False,
    num_workers=0,
)


model = models.resnet18(pretrained=False)
model.fc = nn.Linear(512, 4)
# net = Net(model)
# model.load_state_dict(torch.load('/Users/shaotianyu01/Desktop/school/11.4/6.11.py_best_acc.pth'), False)
# model.load_state_dict(torch.load('/Users/shaotianyu01/Desktop/school/11.4/12.7.py_best_acc.pth'), False)
model.load_state_dict(torch.load('/Users/shaotianyu01/Desktop/bit_model/1.9_4cls_11.pth'), False)

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
net = model.to(DEVICE)

# print('????????????', end='\n\n')
correct = 0
total = 0
list_pred = []
p_ans = []
with torch.no_grad():
    net.eval()
    for i, data in enumerate(test_loader):
        data = data.to(DEVICE)
        y_pred = net(data)
        possibility = y_pred.cpu().numpy().tolist()
        pred = y_pred.argmax(dim=1)
        list_pred += pred.cpu().numpy().tolist()

fenmu = 0
e_list = []
for cur in possibility[0]:
    fenmu += np.exp(cur)
    e_list.append(np.exp(cur))
b = [scores / fenmu for scores in e_list]

label2cn = {'lin': 'lymphoma', 'jiao': 'glioma', 'jia': 'TDLs', 'xue': 'vasculitis'}
for res in list_pred:
    res_cate = label2cate[res]
    print('The predicted result is???{}     The predicted probability is???{:.2f}'.format(label2cn[res_cate], float(max(b))), end='\n\n')

print('The probability of lymphoma is???{:.2f}'.format(float(b[0])), end='\n')
print('The probability of glioma is???{:.2f}'.format(float(b[2])), end='\n')
print('The probability of TDLs is???{:.2f}'.format(float(b[3])), end='\n')
print('The probability of vasculitis is???{:.2f}'.format(float(b[1])), end='\n\n')
print('The forecast results are for reference only')

os.remove(test_root)
# print('?????????????????????:{}'.format(correct / total))
# list_error = []

# print('????????????????????????')
# for i in range(len(list_label)):
#     if list_label[i] != list_pred[i]:
#         img = cv2.imread(list_dir[i])
#         # cv2.imshow('True_label:{}  Pred_label:{}'.format(list_label[i], list_pred[i]), img)
#         # cv2.waitKey(0)
#         list_error.append([list_dir[i], label2cate[list_label[i]], label2cate[list_pred[i]]])
# names = ['????????????', '????????????', '????????????']
#
# print('????????????????????????')
# ans_df = pd.DataFrame(columns=names, data=list_error)
# ans_df.to_csv('/Users/shaotianyu01/Desktop/school/11.4/error.csv')
# print('????????????')
