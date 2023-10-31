import time

out_dir = 'out-bible-psalms-finetuned'
eval_interval = 100
compile = False # takes too little time to finetune, not worth it

# save a nice and overfit checkpoint that
# will only speak Shakespeare and forgets
# everything else about the world #dark
always_save_checkpoint = False

dataset = 'bible_psalms'
init_from = 'gpt2-medium'
batch_size = 1
block_size = 512

learning_rate = 1e-5
max_iters = 3000
decay_lr = True
