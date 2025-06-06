_base_ = [
    '../_base_/models/deformable-detr_r50_16xb2-50e_coco.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
model = dict(
    type='DeformableDETR',
    backbone=dict(
        _delete_=True,
        type='PyramidVisionTransformer',
        num_layers=[2, 2, 2, 2],
        init_cfg=dict(checkpoint='https://github.com/whai362/PVT/'
                      'releases/download/v2/pvt_tiny.pth')),
    neck=dict(in_channels=[64, 128, 320, 512]))
# optimizer
optim_wrapper = dict(
    optimizer=dict(
        _delete_=True, type='AdamW', lr=0.0001, weight_decay=0.0001))
