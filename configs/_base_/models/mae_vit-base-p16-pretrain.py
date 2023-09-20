# model settings
ckpt_path='/archive/hot4/pretrain_model/mae/mae_vit-base-p16_8xb512-fp16-coslr-1600e_in1k_20220825-f7569ca2.pth'
model = dict(
    type='MAE',
    backbone=dict(type='MAEViT', 
                  arch='b', 
                  patch_size=16, 
                  mask_ratio=0.75,
                    init_cfg=dict(
                        type='Pretrained',
                        checkpoint=ckpt_path,
                        prefix='backbone',
                    ),
                  ),
    neck=dict(
        type='MAEPretrainDecoder',
        patch_size=16,
        in_chans=3,
        embed_dim=768,
        decoder_embed_dim=512,
        decoder_depth=8,
        decoder_num_heads=16,
        mlp_ratio=4.,
    ),
    head=dict(
        type='MAEPretrainHead',
        norm_pix=True,
        patch_size=16,
        loss=dict(type='PixelReconstructionLoss', criterion='L2')),
    init_cfg=[
        dict(type='Xavier', layer='Linear', distribution='uniform'),
        dict(type='Constant', layer='LayerNorm', val=1.0, bias=0.0)
    ])
