# -*- coding: utf-8 -*-
"""GAN3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ChpS_RYIdSCsQNR1BNuIc2BEvAHTEGIT
"""

# from torchvision import models
# vgg16 = models.vgg16(pretrained=True)
# # print(vgg16)

import torch
from torch import nn
class generator(nn.Module): 

    #generator model
    def __init__(self):
        super(generator,self).__init__()
        

        self.t1=nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=64,kernel_size=(5,5),stride=1,padding=2),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        
        self.t2=nn.Sequential(
            nn.Conv2d(in_channels=64,out_channels=128,kernel_size=(3,3),stride=2,padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.t3=nn.Sequential(
            nn.Conv2d(in_channels=128,out_channels=128,kernel_size=(3,3),stride=1,padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.t4=nn.Sequential(
            nn.Conv2d(in_channels=128,out_channels=256,kernel_size=(3,3),stride=2,padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i1=nn.Sequential(
            nn.Conv2d(in_channels=256,out_channels=256,kernel_size=(3,3),stride=1,padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i2=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3),padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )

        self.i3=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 2,dilation = 2),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )#bottleneck
        
        self.i4=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 4,dilation = 4),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i5=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 8,dilation = 8),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i6=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 16,dilation = 16),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i7=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i8=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.i9=nn.Sequential(
            nn.ConvTranspose2d(256,128,kernel_size=(4,4), stride = 2,padding = 1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.i10=nn.Sequential(
            nn.Conv2d(128,128,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.i11=nn.Sequential(
            nn.ConvTranspose2d(128,64,kernel_size=(4,4), stride = 2,padding = 1),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.i12=nn.Sequential(
            nn.Conv2d(64,32,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU()
        )
        self.i13=nn.Sequential(
            nn.Conv2d(32,3,kernel_size=(3,3), stride = 1,padding = 1),
            nn.Sigmoid()
        )

        self.m1=nn.Sequential(
            nn.Conv2d(in_channels=256,out_channels=256,kernel_size=(3,3),stride=1,padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.m2=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3),padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )

        self.m3=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 2,dilation = 2),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )#bottleneck
        
        self.m4=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 4,dilation = 4),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.m5=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 8,dilation = 8),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.m6=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), padding = 16,dilation = 16),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.m7=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.m8=nn.Sequential(
            nn.Conv2d(256,256,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.m9=nn.Sequential(
            nn.ConvTranspose2d(256,128,kernel_size=(4,4), stride = 2,padding = 1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.m10=nn.Sequential(
            nn.Conv2d(128,128,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.m11=nn.Sequential(
            nn.ConvTranspose2d(128,64,kernel_size=(4,4), stride = 2,padding = 1),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.m12=nn.Sequential(
            nn.Conv2d(64,32,kernel_size=(3,3), stride = 1,padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU()
        )
        self.m13=nn.Sequential(
            nn.Conv2d(32,1,kernel_size=(3,3), stride = 1,padding = 1),
            nn.Sigmoid()
        )
        
    def forward(self,x):
        
        
        c1 = self.t1(x);
        c2 = self.t2(c1);
        c3 = self.t3(c2);
        br = self.t4(c3);
        
        x = self.i1(br);
        x = self.i2(x);
        x = self.i3(x);
        x = self.i4(x);
        x = self.i5(x);
        x = self.i6(x)
        x = self.i7(x)
        x = self.i8(x)+br;#+t4
        x = self.i9(x)+c3#+t3
        x = self.i10(x)+c2#+t2
        x = self.i11(x)+c1#+t1
        x = self.i12(x);
        op = self.i13(x)
        
        x = self.m1(br);
        x = self.m2(x);
        x = self.m3(x);
        x = self.m4(x);
        x = self.m5(x);
        x = self.m6(x)
        x = self.m7(x)
        x = self.m8(x);
        x = self.m9(x)
        x = self.m10(x)
        x = self.m11(x)
        x = self.m12(x);
        maskop = self.m13(x)
        return op, maskop
        #output of generator


from PIL import Image
import glob
from torch.utils.data import Dataset
from torchvision import transforms
import matplotlib.pyplot as plt

trans = transforms.ToTensor()
class CustomDataSet(Dataset):
    def __init__(self, main_dir , transform):
        self.transform = transform
        self.X_vid = glob.glob('/media/Data2/srivinod/' + main_dir + '/X/*')
        # self.f = 0
    def __len__(self):
        # print('Training ',len(self.X_vid),' videos')
        return len(self.X_vid)

    def __getitem__(self, idx):
        path = self.X_vid[idx]
        x,y = trans(Image.open(path).convert("RGB")), trans(Image.open(path.replace('X', 'Y')).convert("RGB"))
        # self.f = 1-self.f
        # if self.f:
        #     return [torch.flip(x,[1]), torch.flip(y,[1])]
        if self.transform == None:
            return [x,y]
        return [self.transform(x), self.transform(y)]
        # return [x, y,torch.flip(x,[1]), torch.flip(y,[1])]
        # return [torch.cat((x,(x[0,:,:]-y[0,:,:]).unsqueeze(0)), dim = 0), y]
        # return [torch.cat((x,torch.flip(x,[1])), dim = 0), torch.cat((y,torch.flip(y,[1])), dim = 0)] #vertical flip and appending at last

import torch
import torchvision

class VGGPerceptualLoss(torch.nn.Module):
    def __init__(self, resize=True):
        super(VGGPerceptualLoss, self).__init__()
        blocks = []
        blocks.append(torchvision.models.vgg16(pretrained=True).features[:4].eval())
        blocks.append(torchvision.models.vgg16(pretrained=True).features[4:9].eval())
        blocks.append(torchvision.models.vgg16(pretrained=True).features[9:16].eval())
        blocks.append(torchvision.models.vgg16(pretrained=True).features[16:23].eval())
        for bl in blocks:
            for p in bl:
                p.requires_grad = False
        self.blocks = torch.nn.ModuleList(blocks)
        self.transform = torch.nn.functional.interpolate
        self.resize = resize
        self.register_buffer("mean", torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1))
        self.register_buffer("std", torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1))

    def forward(self, input, target, feature_layers=[0, 1, 2, 3], style_layers=[]):
        if input.shape[1] != 3:
            input = input.repeat(1, 3, 1, 1)
            target = target.repeat(1, 3, 1, 1)
        input = (input-self.mean) / self.std
        target = (target-self.mean) / self.std
        if self.resize:
            input = self.transform(input, mode='bilinear', size=(224, 224), align_corners=False)
            target = self.transform(target, mode='bilinear', size=(224, 224), align_corners=False)
        loss = 0.0
        x = input
        y = target
        for i, block in enumerate(self.blocks):
            x = block(x)
            y = block(y)
            if i in feature_layers:
                loss += torch.nn.functional.l1_loss(x, y)
            if i in style_layers:
                act_x = x.reshape(x.shape[0], x.shape[1], -1)
                act_y = y.reshape(y.shape[0], y.shape[1], -1)
                gram_x = act_x @ act_x.permute(0, 2, 1)
                gram_y = act_y @ act_y.permute(0, 2, 1)
                loss += torch.nn.functional.l1_loss(gram_x, gram_y)
        return loss

loss_p = VGGPerceptualLoss().cuda()


import torchvision
import torch
import warnings
warnings.filterwarnings("ignore")

from torch import optim

Batch_Size = 10
my_dataset1 = CustomDataSet('train2', transform = None)
my_dataset2 = CustomDataSet('train2', transform = torchvision.transforms.RandomVerticalFlip(p = 1))
my_dataset3 = CustomDataSet('train2', transform = torchvision.transforms.RandomHorizontalFlip(p = 1))


netG = generator().cuda()
netG.load_state_dict(torch.load('/media/Data2/srivinod/gen2'))
# netD = discriminator().cuda()

# optimizerD = optim.Adam(netD.parameters(), lr=0.002, betas=(0.5, 0.999))
optimizerG = optim.Adam(netG.parameters(), lr=0.002, betas=(0.5, 0.999))
# optimizerG = optim.Adam(list(netG.parameters())+list(vgg16.parameters()), lr=0.002, betas=(0.5, 0.999))

# transI = torchvision.transforms.ToPILImage()
min_loss = 100
d_sets = [my_dataset1, my_dataset2, my_dataset3]
for epoch in range(200):
    l = 0; len_loader = 0   
    for d in d_sets:
        train_loader = torch.utils.data.DataLoader(d , batch_size = Batch_Size, shuffle=True, drop_last = True)
        for i,[inp, tar] in enumerate(train_loader, 0):
            # inp,tar = Variable(inp), Variable(tar)
            #inp, tar = input, target
            inp, tar = inp.cuda(), tar.cuda()
            imitation, mask = netG(inp)
            # print(mask.repeat((1,3,1,1)).shape)
            completion = imitation*mask.repeat((1,3,1,1))+inp*(1-mask.repeat((1,3,1,1)))
            maskin = torch.abs(inp-tar)
            maskin[maskin<=0.21]=0
            maskin[maskin>0.21]=1
            maskin = torch.sum(maskin,dim=1)
            maskin[maskin>0] = 1;maskin = maskin.unsqueeze(1)
            
            optimizerG.zero_grad()
            cur_l1 = torch.nn.L1Loss()(mask, maskin);
            cur_l2 = 10*torch.nn.L1Loss()(mask*imitation, mask*tar) + torch.nn.L1Loss()((1-mask)*imitation, (1-mask)*tar) + torch.nn.L1Loss() (completion, tar)
            cur_l = cur_l1 + cur_l2 + 1e-10 * loss_p(tar, imitation)
            cur_l.backward();
            optimizerG.step()
            
            l += torch.mean(cur_l1).item() + torch.mean(cur_l2).item()
            # if i%50==0:
            #     print(i,end=' ')
        len_loader += len(train_loader)
        # print(round(r/(2*len(train_loader)),2),round(f/(2*len(train_loader)),2),round(l.item()/(2*len(train_loader)),4))
    print(round(l/len_loader,4))
    if(min_loss>l/len_loader):
        torch.save(netG.state_dict(), '/media/Data2/srivinod/gen_perc')
        min_loss = l/len_loader


