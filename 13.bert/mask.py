import torch

import data


def get_key_padding_mask(x):
    # b句话,每句话60个词,这里是还没embed的
    # x = [b, 60]
    # 判断每个词是不是<PAD>
    mask = x == data.zidian['<PAD>']

    return mask


'''
tensor([[False,  True,  True,  True,  True],
        [False, False,  True,  True,  True],
        [False, False, False,  True,  True],
        [False, False, False, False,  True],
        [False, False, False, False, False]])'''
attn_mask = torch.triu(torch.ones((60, 60), dtype=torch.long), diagonal=1)
attn_mask = attn_mask == 1

print(attn_mask)

a =2

if __name__ == '__main__':
    print(attn_mask)
    print(get_key_padding_mask(torch.ones(2, 5)))
